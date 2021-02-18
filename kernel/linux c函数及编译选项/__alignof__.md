# \__alignof__

- 用于对象、函数、类型对齐

- 和sizeof类似或C11的  **\_Alignof**，如**\__alignof__ **(double) = 8

- 举例：long double 结构就有不同的布局

  - long double 类型的变量在 x86 平台上是按照 4 个字节进行对齐的。

  - 在 POWER 平台上则是按照 8 个字节进行对齐的

- 如果参数为一个函数，**\__alignof__(func) **表达式的计算结果为函数的对齐，可以通过属性aligned指定该函数

作用: 不要将大小和偏移量都在编码中写死。





**宏 `offsetof` **

- 是一个变量，它可以获取结构程序从该结构开始地址处的偏移量。



**sizeof**

- C 语言中的 `sizeof` 操作可以查询基本类型和复杂类型的大小



```c
struct foo{
        int  x;
        char y;
}foo1;

int main()
{
        printf("__alignof__(x):%u __alignof__(y):%u\n", __alignof__(foo1.x), __alignof__(foo1.y));

        return 0;
}

/* __alignof__(x):4 __alignof__(y):1 
 * 这里尽管foo1.y的实际对齐可能2或 4，和__alignof__(int)一致，(应该只能是4吧)。
 */
```

[http://gcc.gnu.org/onlinedocs/gcc/Alignment.html](http://gcc.gnu.org/onlinedocs/gcc/Alignment.html)



[**linux内核代码中\__alignof__ 对齐**](https://blog.csdn.net/chdhust/article/details/8602627)