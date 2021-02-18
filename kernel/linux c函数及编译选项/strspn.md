# strspn

**描述**

**size_t strspn(const char \*str1, const char \*str2)** 检索字符串 **str1** 中第一个不在字符串 **str2** 中出现的字符下标。



**原型**

```c
/*
 * @param str1 要被检索的 C 字符串
 * @param str2 该字符串包含了要在 str1 中进行匹配的字符列表。
 * 
 * @return 该函数返回 str1 中第一个不在字符串 str2 中出现的字符下标。
*/
size_t strspn(const char *str1, const char *str2)
```

**实例**

```c
#include <stdio.h>
#include <string.h>

int main ()
{
   int len;
   const char str1[] = "ABCDEFG019874";
   const char str2[] = "ABCD";

   /*
    * 通常用于检测字符串前面是否有\t 、' '等多余空白。
   */
   len = strspn(str1, str2);

   printf("初始段匹配长度 %d, str1: %s\n", len, str1+len);
   
   return(0);
}
/*
 * 初始段匹配长度 4, str1: EFG019874
*/
```

