# 集合
# 1. 集合
# 集合是可变序列，集合中的元素是无序的，不重复的，集合中的元素是唯一的，集合中的元素是不可变的。
# 无序，也就是定义和取出的顺序不能保持一致。集合底层会按照自己的一套算法来存储和取数据，所以每次取出顺序是不变的
#       取出可能和定义的顺序不一致，但是以后再取出顺序是一致的
# 由于无序，所以不能使用索引和切片

# 2. 集合对象支持集合操作，如交集、并集、差集等。


# 3. 既然有了列表，元组，字符串，为什么还要有集合？
# 集合的元素是唯一的，列表的元素可以重复，集合的元素是无序的，列表的元素是有序的。
# 集合的元素是不可变的，列表的元素是可变的。

#  集合的定义 语法：
# 集合名 = {元素1, 元素2, 元素3, ...}
# 例子：
set1 = {1, 2, 3, 4, 5, 4}
print(set1)
print(type(set1))

# 创建空集合 语法：set()，不能使用set1 = {}，因为这样会创建一个字典
set2 = set()
print(f"空集合：{set2}, 类型：{type(set2)}")
set3 = {}
print(f"字典：{set3}, 类型：{type(set3)}")

# 集合的遍历， 只能使用for循环
for item in set1:
    print(item)


# 集合的常用方法和操作详解
# 1. 使用.add()方法添加元素，无序添加，添加后不保证顺序
set1.add(6)
print(f"添加元素后：{set1}")
# 2. 使用.remove()方法删除元素
set1.remove(3)
print(f"删除元素后：{set1}")
# 3. 使用.clear()方法清空集合
# set1.clear()
print(f"清空集合后：{set1}")
# 4. 使用.copy()方法复制集合
set4 = set1.copy()
print(f"复制集合后：{set4}")
# 5. 使用len()方法统计元素个数，去重后的元素个数
length = len(set1)
print(f"集合元素个数：{length}")
# 6. 使用.max()方法查找最大值
max = max(set1)
print(f"集合最大值：{max}")
# 7. 使用.min()方法查找最小值
min = min(set1)
print(f"集合最小值：{min}")
# 8. 使用.in和not in判断元素是否存在
print(f"元素1是否存在：{1 in set1}")
print(f"元素10是否存在：{10 in set1}")
# 9. 使用pop()方法从集合中移除并返回一个元素，集合是无序的，所以每次移除的元素是随机的
print(f"移除的元素：{set1.pop()}")
print(f"移除的元素：{set1.pop()}")
print(f"移除元素后：{set1}")
# 10. 使用union()方法合并集合，另一种写法为set1 | set4
print(f"set1：{set1}")
print(f"set4：{set4}")
set6 = set1.union(set4)
print(f"合并集合后：{set6}")
# 11. 使用intersection()方法求交集，另一种写法为set1 & set4
set7 = set1.intersection(set4)
print(f"交集：{set7}")
# 12. 使用difference()方法求差集，另一种写法为set1 - set4
set8 = set1.difference(set4)
print(f"差集：{set8}")
# 13. 使用symmetric_difference()方法求对称差集，另一种写法为set1 ^ set4
set4.add(7)
set9 = set1.symmetric_difference(set4)
print(f"对称差集：{set9}")


# 集合生成式
# 语法：
# 集合名 = {表达式 for 变量 in 可迭代对象}
# 例子：
set10 = {i for i in range(1, 11)}
print(f"集合生成式：{set10}")
