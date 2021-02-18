# linux内核常见宏

**参考**

[1 - Linux内核常见宏的作用 ](https://www.sohu.com/a/277984306_654301)

```c
/*
 * #define__init __attribute__ ((__section__ (".init.text")))
 * 	这个标志符和函数声明放在一起，表示gcc编译器在编译时，需要把这个函数放在.text.init Section 中，
 *  而这个Section 在内核完成初始化 之后，就会被释放掉。
 * #define__initdata __attribute__ ((__section__ (".init.data")))
 * 	这个标志符和变量声明放在一起，表示gcc编译器在编译时，需要把这个变量放在.data.init Section中，
 * 	而这个Section 在内核完成初始化之后，会释放掉。
 * #define asmlinkage CPP_ASMLINKAGE __attribute__((regparm(0)))
 * 	这个标志符和函数声明放在一起，带regparm(0)的属性声明告诉gcc编译器，
 *	该函数不需要通过任何寄存器来传递参数，参数只是通过堆栈来传递。
 *  gcc编译器在汇编过程中调用c语言函数时传递参数有两种方法：一种是通过堆栈，另一种是通过寄存器。
 *	缺省时采用寄存器，假如你要在你的汇编过程中调用c语言函数，并且想通过堆栈传递参数，你定义的 c 函数时要在函数前加上宏asmlinkage。
 *  
 *  其他参考 上述链接 [1]
*/

/*
 * 如下宏定义在： kernel/include/linux/init.h
 * 其中： # define __section(S) __attribute__ ((__section__(#S)))
*/

/* These are for everybody (although not all archs will actually
   discard it in modules) */
#define __init      __section(.init.text) __cold notrace
#define __initdata  __section(.init.data)
#define __initconst __constsection(.init.rodata)
#define __exitdata  __section(.exit.data)
#define __exit_call __used __section(.exitcall.exit)


#define __exit          __section(.exit.text) __exitused __cold notrace

/* For assembly routines */
#define __HEAD      .section    ".head.text","ax"
#define __INIT      .section    ".init.text","ax"
#define __FINIT     .previous

#define __INITDATA  .section    ".init.data","aw",%progbits
#define __INITRODATA    .section    ".init.rodata","a",%progbits
#define __FINITDATA .previous

#define __CPUINIT        .section   ".cpuinit.text", "ax"
#define __CPUINITDATA    .section   ".cpuinit.data", "aw"
#define __CPUINITRODATA  .section   ".cpuinit.rodata", "a"

#define __MEMINIT        .section   ".meminit.text", "ax"
#define __MEMINITDATA    .section   ".meminit.data", "aw"
#define __MEMINITRODATA  .section   ".meminit.rodata", "a"

/* silence warnings when references are OK */
#define __REF            .section       ".ref.text", "ax"
#define __REFDATA        .section       ".ref.data", "aw"
#define __REFCONST       .section       ".ref.rodata", "a"
```

