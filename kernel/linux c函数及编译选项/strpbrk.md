# strpbrk

**描述**

C 库函数 **char \*strpbrk(const char \*str1, const char \*str2)**  检索字符串 **str1** 中第一个匹配字符串 **str2** 中字符的字符，不包含空结束字符。也就是说，依次检验字符串 str1 中的字符，当被检验字符在字符串 str2 中也包含时，则停止检验，并返回该字符位置。

**原型**

```c
/*
 * @param str1 要被检索的 C 字符串。
 * @param str2 该字符串包含了要在 str1 中进行匹配的字符列表。
 * 
 * @return 该函数返回 str1 中第一个匹配字符串 str2 中字符的字符数，如果未找到字符则返回 NULL。
*/
char *strpbrk(const char *str1, const char *str2)
```

**实例**

```c
#include <stdio.h>
#include <string.h>
 
int main ()
{
   const char str1[] = "abcde2fghi3jk4l";
   const char str2[] = "34";
   char *ret;
 
   /*
    * 可用于字符串检测是否包含特殊字符等，如检测是否包含 !#\"\\ 这些字符中任意一个。
   */
   ret = strpbrk(str1, str2);
   if(ret) 
   {
      printf("第一个匹配的字符是： %c\n", *ret);
   }
   else 
   {
      printf("未找到字符");
   }
   
   return(0);
}
/*
 * 第一个匹配的字符是： 3
*/
```

