s1 = 'helo, word'
s2 = "helo,  word"

# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
helo,
wo  rd
'''
print(s1, s2, s3, end='')

s4 = '\'helo word\''     # 'helo word'
s5 = '\n\\helo word\\\n' # \helo word\
print(s4, s5, end = '')

s6 = r'\'hello, world!\''     # \'hello, world!\'
s7 = r'\n\\hello, world!\\\n' # \n\\hello, world!\\\n
print(s6, s7, end='')

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))

# 字符串提供的方法来完成字符串的格式
print('{0} * {1} = {2}'.format(a, b, a * b))

# 字符串前加上字母f来简化
print(f'{a} * {b} = {a * b}')