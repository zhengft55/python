# Python中的加号（+）运算符使用详解

# 1. 数值相加
a = 5
b = 10
result = a + b
print("数值相加：", a, "+", b, "=", result)  # 输出：数值相加： 5 + 10 = 15

# 2. 字符串拼接
str1 = "Hello"
str2 = "World"
str_result = str1 + " " + str2
# 输出：字符串拼接： Hello + World = Hello World
print("字符串拼接：", str1, "+", str2, "=", str_result)

# 3. 列表合并
list1 = [1, 2, 3]
list2 = [4, 5]
list_result = list1 + list2
# 输出：列表合并： [1, 2, 3] + [4, 5] = [1, 2, 3, 4, 5]
print("列表合并：", list1, "+", list2, "=", list_result)

# 4. 元组合并
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple_result = tuple1 + tuple2
# 输出：元组合并： (1, 2) + (3, 4) = (1, 2, 3, 4)
print("元组合并：", tuple1, "+", tuple2, "=", tuple_result)

# 5. 不同类型不能直接相加（会报错）
# 下面的代码会报错：TypeError: can only concatenate str (not "int") to str
# print("数字和字符串相加：", "abc" + 123)

# 正确做法：需要类型转换
print("数字和字符串拼接（类型转换）：", "abc" + str(123))  # 输出：abc123

# 6. 复合赋值运算符 +=
num = 10
num += 5  # 等价于 num = num + 5
print("使用+=后num的值：", num)  # 输出：15

# 字符串也可以用+=拼接
s = "Hello"
s += " Python"
print("字符串用+=拼接：", s)  # 输出：Hello Python

# 总结：
# + 在Python中不仅可以用于数值相加，还可以用于字符串拼接、列表/元组合并等。
# 但不同类型之间不能直接相加，需注意类型转换。
