# Linux网络收包流程

参考：[Linux网络收包流程-wx](https://mp.weixin.qq.com/s?__biz=MzI3NzA5MzUxNA==&mid=2664608340&idx=1&sn=3210e6bf864df867326308cdf0f13515&chksm=f04d9fb1c73a16a7d02c98af109f945e27bcaadd24f909f9062d5e00924ef8ccc2c156d68dc4&scene=126&sessionid=1597904669&key=b17219827522b0146a6402e8672b4384ca5a0cffd0021d4b7cba1515fc6b17709bf41505b5b6a9b30c82327b614199ef3d2919fca217fdff58c85cf9051cac763df3b059b8ff07d6c5d2b2172e208568f534544d5e1d77722ba80913ba6daebd897f463a0136bab06112d366cec7c99916747ff459b32a9b21dd4181727ab34e&ascene=1&uin=MTU3NzAwNTgyMQ%3D%3D&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&exportkey=AWOVHKqK%2FVPTsRW1hh%2Fbj7c%3D&pass_ticket=v%2BHRZzvhkDPHzXJdNth9wWuyEa8FFpaAAc0fBVDorpW%2B%2B%2Bz8%2FbXTa%2FElpTe1%2FOWc)

 Linux(2.6.11.12)网络收包流程图：

<img src="D:\documents\1 - summary\linux内核学习笔记\linux内核网络\linux网络收包流程_blog.png" alt="image-20200821100229457" style="zoom:50%;" />

```c

  device driver interrupt handler
       netif_rx()
              cpu_raise_softirq()
                     do_softirq()
net_rx_atcion()
      dev->poll(dev, &budget)( process_backlog)（注0）

      process_backlog()
   netif_receive_skb()
       skb_bond(skb); 如果网卡绑定，则取netdev 的master设备
       pt_prev->func() （注1）
       type = skb->protocol(L3层 ipv4 or ipv6 ..)
          ip_rcv()
             NF_HOOK(PF_INET,NF_IP_PRE_ROUTING,skb, dev, NULL,ip_rcv_finish);
               ip_rcv_finish()
                   dst_input()
                     skb->dst->input();(注2)
                        （ip_local_deliver或ip_forward）
                           ip_local_deliver()
                              NF_HOOK(PF_INET,NF_IP_LOCAL_IN, skb, skb->dev, NULL,
                                ip_local_deliver_finish);
                                    ip_local_deliver_finish()
                                        ipprot->handler(skb);
                                        （L4层 udp_rcv/tcp_v4_rcv..）
                                         udp_rcv()
                                           udp_queue_rcv_skb()
                                              sock_queue_rcv_skb
                                               sk->sk_data_ready()                   （sock_def_readable）

                                                             
static void sock_def_readable(structsock *sk, int len)

{

       read_lock(&sk->sk_callback_lock);
       if (sk->sk_sleep && waitqueue_active(sk->sk_sleep))
               wake_up_interruptible(sk->sk_sleep);
       sk_wake_async(sk,1,POLL_IN);
       read_unlock(&sk->sk_callback_lock);
}

                                                                     
sys_recvfrom()
       sock_recvmsg()
              sock->ops->recvmsg()（sock_common_recvmsg）
              sock_common_recvmsg()
                     sk->sk_prot->recvmsg()(udp_recvmsg)
                     udp_recvmsg()
                            skb_recv_datagram()
                                   wait_for_packet()
   
static int wait_for_packet(structsock *sk, int *err, long *timeo_p)
{
…
  DEFINE_WAIT(wait);
  prepare_to_wait_exclusive(sk->sk_sleep,&wait,TASK_INTERRUPTIBLE);
…
}
注0：
net_dev_init()
{
  …
  queue->backlog_dev.poll = process_backlog;
  …
}
注1：
void __init ip_init(void)
{
  dev_add_pack(&ip_packet_type);
}
static struct packet_type ip_packet_type = {
        .type = __constant_htons(ETH_P_IP),
        .func = ip_rcv,
};
void __init ipv6_packet_init(void)
{
        dev_add_pack(&ipv6_packet_type);
}

static struct packet_type ipv6_packet_type = {
        .type = __constant_htons(ETH_P_IPV6),
        .func = ipv6_rcv,
};

void dev_add_pack(struct packet_type *pt)
{
  …
  list_add_rcu(&pt->list, &ptype_base[hash]);
 …
}

注2:
ip_rcv_finish
  ip_route_input
    ip_route_input_slow
ip_route_input_slow()
{
  …
  rth->u.dst.input = ip_forward;
  …
  rth->u.dst.input= ip_local_deliver;
}

```

