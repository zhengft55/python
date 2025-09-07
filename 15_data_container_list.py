# 数据容器
# 1. 列表
# 2. 元组
# 3. 字符串
# 4. 集合
# 5. 字典

# 1. 列表
# 语法：
# 列表名 = [元素1, 元素2, 元素3, ...]
# 注意：列表中的元素可以是不同的数据类型，元素可以有多个，允许有重复的元素，并且是有序的
# 例子：
list1 = [1, 2, '3', 4, 5]
list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))
# 列表的索引
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
# 列表的切片
print(list1[0:2])
print(list1[2:4])
print(list1[4:])
print(list1[:4])
print(list1[:])
print(list1[::2])
print(list1[1::2])
print(list1[::-1])
# 列表的增删改查
list1.append(6)

# while循环遍历列表
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
# for循环遍历列表
for item in list1:
    print(item)
# 列表的排序
list1.sort()

# 构建空列表
list2 = []
list3 = list()
# 构建包含多个元素的列表
list4 = [1, 2, 3, 4, 5]
list5 = list(range(1, 6))

# 列表的索引可以为负数，表示从后往前数
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
# 列表的切片可以为负数，表示从后往前数
print(list1[-1:])
print(list1[-2:])
print(list1[-3:])

# 列表的常用方法和操作详解：

# 1. 通过索引修改列表中的元素
list1[0] = 10  # 修改第一个元素
print(f"修改后的列表：{list1}")

# 2. 使用.append()方法添加元素（在列表末尾添加一个元素）
list1.append(7)
print(f"添加元素后：{list1}")

# 3. 使用.remove()方法删除元素（删除第一个匹配的元素）
list1.remove(3)  # 删除值为3的元素
print(f"删除元素后：{list1}")

# 4. 使用.pop()方法删除元素（删除指定索引的元素，默认删除最后一个）
removed_item = list1.pop()  # 删除最后一个元素并返回
print(f"删除的元素：{removed_item}")
print(f"删除后的列表：{list1}")

# 5. 使用.clear()方法清空列表
list_copy = list1.copy()  # 先复制一份用于演示
list_copy.clear()
print(f"清空后的列表：{list_copy}")

# 6. 使用.insert()方法插入元素（在指定位置插入元素）
list1.insert(0, 0)  # 在索引0位置插入元素0
print(f"插入元素后：{list1}")

# 7. 使用.extend()方法扩展列表（将另一个可迭代对象的元素添加到列表末尾）
list1.extend([8, 9, 10])
print(f"扩展列表后：{list1}")

# 8. 使用.sort()方法排序（原地排序，直接修改原列表）
list1.sort()
print(f"排序后：{list1}")

# 9. 使用.reverse()方法反转列表（原地反转）
list1.reverse()
print(f"反转后：{list1}")

# 10. 使用.count()方法统计元素个数
count = list1.count(2)  # 统计值为2的元素出现次数
print(f"元素2出现的次数：{count}")

# 11. 使用.index()方法查找元素索引（返回第一个匹配元素的索引）
try:
    index = list1.index(5)  # 查找值为5的元素的索引
    print(f"元素5的索引：{index}")
except ValueError:
    print("元素5不在列表中")

# 12. 使用len()函数统计列表长度（注意：不是.len()方法）
length = len(list1)
print(f"列表长度：{length}")

# 13. 使用max()函数查找列表最大值（注意：不是.max()方法）
if list1:  # 确保列表不为空
    maximum = max(list1)
    print(f"列表最大值：{maximum}")

# 14. 使用min()函数查找列表最小值（注意：不是.min()方法）
if list1:  # 确保列表不为空
    minimum = min(list1)
    print(f"列表最小值：{minimum}")

# del 语句删除列表中的元素，del和pop的区别是，del是删除指定索引的元素，pop是删除指定索引的元素，并返回该元素，和remove的区别是，remove是删除指定值的元素，和clear的区别是，clear是清空列表，而del是删除列表
print(f"删除元素前：{list1}")
del list1[0]
print(f"删除元素后：{list1}")
# del list1
# print(f"删除列表后：{list1}")


# 列表是可变序列，str和int是不可变序列，列表作为参数传递时，是地址传递，而str和int作为参数传递时，是值传递（重点）

# 列表生成式：
# 语法：
# 列表名 = [表达式 for 变量 in 可迭代对象]
# 例子：
list6 = [i for i in range(1, 11)]
print(f"列表生成式：{list6}")
# 列表生成式可以嵌套，但是不推荐
list7 = [i for i in range(1, 11) if i % 2 == 0]
print(f"列表生成式：{list7}")
list8 = [i+i for i in range(1, 11)]
print(f"列表生成式：{list8}")
