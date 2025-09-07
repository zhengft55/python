# 元组
# 语法：
# 元组名 = (元素1, 元素2, 元素3, ...)
# 注意：元组中的元素可以是不同的数据类型，元素可以有多个，允许有重复的元素，并且是有序的
# 例子：
tuple1 = (1, 2, '3', 4, 5)
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))
# 元组的索引
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
# 元组的切片
print(tuple1[0:2])
print(tuple1[2:4])
print(tuple1[4:])
print(tuple1[:4])
print(tuple1[:])
print(tuple1[::2])
print(tuple1[1::2])
print(tuple1[::-1])

# 元组和列表的区别：
# 1. 元组是不可变序列，列表是可变序列，元组中的元素不能修改，列表中的元素可以修改。没有append、remove、pop、clear、insert、sort、reverse方法
# 2. 元组使用小括号，列表使用中括号
# 3. 元组只有一个元素时，需要在元素后面加逗号，列表不需要
# 4. 元组使用tuple()函数创建，列表使用list()函数创建
# 5. 元组使用+号连接，列表使用extend()方法连接
# 6. 元组和列表都可以使用*号进行重复操作（创建包含重复元素的新序列）
# 元组重复示例：
tuple_repeat = (1, 2) * 3  # 结果：(1, 2, 1, 2, 1, 2)
print(f"元组重复操作：{tuple_repeat}")
# 列表重复示例：
list_repeat = [1, 2] * 3  # 结果：[1, 2, 1, 2, 1, 2]
print(f"列表重复操作：{list_repeat}")
# 注意：重复操作会创建新的序列，不会修改原序列
# 7. 元组使用in和not in判断元素是否存在，列表使用in和not in判断元素是否存在
# 8. 元组使用len()函数统计元素个数，列表使用len()函数统计元素个数

# 元组使用语法 元组名[索引]
print(tuple1[0])
# 元组的遍历 for 和 while
# for循环遍历元组
for item in tuple1:
    print(item)
# while循环遍历元组
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1


# 创建空元组
tuple2 = ()
tuple3 = tuple()
# 创建包含多个元素的元组
tuple4 = (1, 2, 3, 4, 5)
tuple5 = tuple(range(1, 6))

# 元组的索引可以为负数，表示从后往前数
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])
print(tuple1[-4])
print(tuple1[-5])
# 元组的切片可以为负数，表示从后往前数
print(tuple1[-1:])
print(tuple1[-2:])
print(tuple1[-3:])

# 索引是从0开始，切片是从1开始。索引必须在指定范围内
# print(tuple1[10])

# 元组是不可变序列，不能修改元组中的元素（重点）
# tuple1[0] = 10

# 可以修改list中的元素，但是不能修改tuple中的元素，因为tuple是不可变序列，list是可变序列
# 可以修改元组内list中的元素（包括修改，增加，删除），因为list是可变序列
tuple6 = (1, 2, [3, 4, 5])
tuple6[2][0] = 10
print(f"修改后的元组：{tuple6}")
# 可以修改元组内tuple中的元素（包括修改，增加，删除），因为tuple是不可变序列
tuple7 = (1, 2, (3, 4, 5))
# tuple7[2][0] = 10
# print(f"修改后的元组：{tuple7}")

# 索引可以从后往前数，最后一个元素的索引是-1
print(tuple1[-1])

# 定义 只有一个元素的元组，需要在元素后面加逗号，否则会被认为是普通数据类型
tuple8 = (1,)
print(f"只有一个元素的元组：{tuple8}")
# 定义 只有一个元素的元组，需要在元素后面加逗号，否则会被认为是普通数据类型
tuple9 = (1)
print(f"只有一个元素的元组：{tuple9}")
# 定义 只有一个元素的元组，需要在元素后面加逗号，否则会被认为是普通数据类型

# 元组和列表的转换
list1 = list(tuple1)
print(f"元组转换为列表：{list1}")

# 元组的常用操作一览
# 1. 使用.count()方法统计元素个数
count = tuple1.count(1)
print(f"元素1出现的次数：{count}")
# 2. 使用.index()方法查找元素索引（返回第一个匹配元素的索引）
index = tuple1.index(1)
print(f"元素1的索引：{index}")
# 3. 使用len()函数统计元素个数
length = len(tuple1)
print(f"元组长度：{length}")
# 4. 使用max()函数查找元组最大值
max_value = max(tuple1)
print(f"元组最大值：{max_value}")
# 5. 使用min()函数查找元组最小值
min_value = min(tuple1)
print(f"元组最小值：{min_value}")
# 6. 使用sum()函数求和
sum_value = sum(tuple1)
print(f"元组求和：{sum_value}")
