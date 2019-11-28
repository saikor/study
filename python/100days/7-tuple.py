'''
为什么还需要元组这样的类型呢？

    1、元组中的元素是无法修改的，
事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象。
一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，
简单的说就是一个不变的对象要比可变的对象更加容易维护；
另一方面因为没有任何一个线程能够修改不变对象的内部状态，
一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。
一个不变对象可以方便的被共享访问。
所以结论就是：如果不需要对元素进行添加、删除、修改的时候，
可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。
    2、元组在创建时间和占用的空间上面都优于列表。
我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，
这个很容易做到。我们也可以在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间。
'''


# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)

'''
    元组的元素不能修改
'''
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError

import sys

# 将元组转换成列表
person = list(t)
# 列表是可以修改它的元素的
person[0] = '李小龙'
print(person)

print('sizeof tuple: ', sys.getsizeof(t), end='\n')
print('sizeof list : ', sys.getsizeof(person), end='\n')

# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)