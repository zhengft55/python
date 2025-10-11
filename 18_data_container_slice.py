# 切片
# 切片是用于获取序列的子集，序列可以是列表、元组、字符串等
# 切片语法：序列[start:end:step]
# start: 起始索引，包含该索引，不写默认是0
# end: 结束索引，不包含该索引，不写默认是最后一个
# step: 步长，默认为1
# 切片示例：str， tuple， list
str1 = "Hello, World!"
print(str1[1:3])
print(str1[1:3:2])
print(str1[1:])
print(str1[:3])
print(str1[:])
print(str1[::2])
print(str1[1::2])
print(str1[::-1])
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[1:3])
print(tuple1[1:3:2])
print(tuple1[1:])
print(tuple1[:3])
print(tuple1[:])
print(tuple1[::2])
print(tuple1[1::2])
print(tuple1[::-1])
list1 = [1, 2, 3, 4, 5]
print(list1[1:3])
print(list1[1:3:2])
print(list1[1:])
print(list1[:3])
print(list1[:])
print(list1[::2])
print(list1[1::2])
print(list1[::-1])

# 步长可以为负数，表示从后往前数，同时注意开始索引和结束索引也要反向标记
print(str1[::-1])
print(tuple1[::-1])
print(list1[::-1])

str = "123456"
print(str[-1:-6:-2])

# 切片操作不会影响原序列，会创建新的序列
# 例子：
list2 = [10, 20, 30, 40, 50]
sub_list = list2[1:4]  # 取索引1到3的元素，结果是[20, 30, 40]
print(f"原列表：{list2}")
print(f"切片后的新列表：{sub_list}")
# 修改新列表不会影响原列表
sub_list[0] = 999
print(f"修改新列表后：{sub_list}")
print(f"原列表依然不变：{list2}")
print(list2[-1:-4:-1][-1:-4:-1])
# 或者使用.reverse()方法
list3 = list2[-1:-4:-1]
list3.reverse()
print(list3)
