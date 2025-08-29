# 算术运算符
# Python中的基本算术运算符包括：+、-、*、/、//、%、**

print("=== 1. 基本算术运算符 ===")
a = 10
b = 3

# 加法运算符 +
result_add = a + b
print(f"{a} + {b} = {result_add}")  # 输出：10 + 3 = 13

# 减法运算符 -
result_sub = a - b
print(f"{a} - {b} = {result_sub}")  # 输出：10 - 3 = 7

# 乘法运算符 *
result_mul = a * b
print(f"{a} * {b} = {result_mul}")  # 输出：10 * 3 = 30

# 除法运算符 /（返回浮点数）
result_div = a / b
print(f"{a} / {b} = {result_div}")  # 输出：10 / 3 = 3.3333333333333335

# 整数除法运算符 //（向下取整）
result_floor_div = a // b
print(f"{a} // {b} = {result_floor_div}")  # 输出：10 // 3 = 3

# 取模运算符 %（求余数）
# 取模运算的数学公式：a % b = a - (a // b) * b
# 其中 a 是被除数，b 是除数，// 是整数除法（向下取整）
# 例如：10 % 3 = 10 - (10 // 3) * 3 = 10 - 3 * 3 = 10 - 9 = 1
result_mod = a % b
print(f"{a} % {b} = {result_mod}")  # 输出：10 % 3 = 1

# 幂运算符 **（求幂）
result_pow = a ** b
print(f"{a} ** {b} = {result_pow}")  # 输出：10 ** 3 = 1000

print("\n=== 2. 浮点数运算示例 ===")
x = 15.5
y = 4.2

print(f"{x} + {y} = {x + y}")  # 19.7
print(f"{x} - {y} = {x - y}")  # 11.3
print(f"{x} * {y} = {x * y}")  # 65.1
print(f"{x} / {y} = {x / y}")  # 3.6904761904761907
print(f"{x} // {y} = {x // y}")  # 3.0
print(f"{x} % {y} = {x % y}")  # 3.0000000000000004

print("\n=== 3. 负数运算示例 ===")
m = -8
n = 3

print(f"{m} + {n} = {m + n}")  # -5
print(f"{m} - {n} = {m - n}")  # -11
print(f"{m} * {n} = {m * n}")  # -24
print(f"{m} / {n} = {m / n}")  # -2.6666666666666665
print(f"{m} // {n} = {m // n}")  # -3（向下取整）
print(f"{m} % {n} = {m % n}")  # 1（负数取模的结果符号与除数相同）

print("\n=== 4. 运算符优先级示例 ===")
# 优先级（从高到低）：** > *、/、//、% > +、-
result1 = 2 + 3 * 4  # 先算乘法，后算加法
print(f"2 + 3 * 4 = {result1}")  # 14

result2 = (2 + 3) * 4  # 括号优先级最高
print(f"(2 + 3) * 4 = {result2}")  # 20

result3 = 2 ** 3 * 4  # 先算幂运算，后算乘法
print(f"2 ** 3 * 4 = {result3}")  # 32

result4 = 10 / 2 * 3  # 同优先级从左到右
print(f"10 / 2 * 3 = {result4}")  # 15.0

print("\n=== 5. 特殊情况处理 ===")
# 除零错误
try:
    error_result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误：{e}")

# 整数除法除零
try:
    error_result2 = 10 // 0
except ZeroDivisionError as e:
    print(f"整数除法除零错误：{e}")

# 大数运算
big_num1 = 123456789
big_num2 = 987654321
print(f"大数相乘：{big_num1} * {big_num2} = {big_num1 * big_num2}")

print("\n=== 6. 字符串与算术运算符 ===")
# 字符串可以使用 + 和 * 运算符
str1 = "Hello"
str2 = "World"
print(f"字符串拼接：'{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")
print(f"字符串重复：'{str1}' * 3 = '{str1 * 3}'")


print("\n=== 7. 比较运算符示例 ===")
# 比较运算符用于比较两个值，返回布尔值（True或False）
# 包括：==（等于）、!=（不等于）、>（大于）、<（小于）、>=（大于等于）、<=（小于等于）、is（对象身份）、is not（对象身份不等于）

# 数值比较示例
x = 10
y = 20
z = 10

print(f"{x} == {y}: {x == y}")    # False，10不等于20
print(f"{x} == {z}: {x == z}")    # True，10等于10
print(f"{x} != {y}: {x != y}")    # True，10不等于20
print(f"{x} > {y}: {x > y}")      # False，10不大于20
print(f"{x} < {y}: {x < y}")      # True，10小于20
print(f"{x} >= {z}: {x >= z}")    # True，10大于等于10
print(f"{x} <= {y}: {x <= y}")    # True，10小于等于20

# 字符串比较示例
str1 = "apple"
str2 = "banana"
str3 = "apple"

print(f"'{str1}' == '{str2}': {str1 == str2}")  # False
print(f"'{str1}' == '{str3}': {str1 == str3}")  # True
print(f"'{str1}' < '{str2}': {str1 < str2}")    # True，按字母序比较

# is 和 is not 运算符（比较对象身份，即内存地址）
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")        # True，内容相同
print(f"a is b: {a is b}")        # False，不是同一个对象
print(f"a is c: {a is c}")        # True，是同一个对象
print(f"a is not b: {a is not b}")  # True，不是同一个对象

print(f"{str1} is {str3}: {str1 is str3}")        # True，字符串驻留机制

# 小整数和字符串的特殊情况（Python的优化机制）
num1 = 100
num2 = 100
print(f"num1 is num2 (小整数): {num1 is num2}")  # True，小整数会被缓存

large1 = 1000
large2 = 1000
print(f"large1 is large2 (大整数): {large1 is large2}")  # 可能是False

# 链式比较
score = 85
print(f"80 <= {score} <= 90: {80 <= score <= 90}")  # True，可以连续比较
print(f"90 < {score} < 100: {90 < score < 100}")    # False


# 逻辑运算符
# and、or、not 用于组合和修改条件表达式

# and 运算符（与）- 所有条件都为True时结果才为True
age = 25
has_license = True
has_car = False

# True，两个条件都满足
print(f"age >= 18 and has_license: {age >= 18 and has_license}")
# False，has_car为False
print(f"age >= 18 and has_car: {age >= 18 and has_car}")

# or 运算符（或）- 任意一个条件为True时结果就为True
is_weekend = True
is_holiday = False

# True，其中一个为True
print(f"is_weekend or is_holiday: {is_weekend or is_holiday}")
# True，has_license为True
print(f"has_car or has_license: {has_car or has_license}")

# not 运算符（非）- 取反操作
is_raining = False
# True，False的反面是True
print(f"not is_raining: {not is_raining}")
# False，True的反面是False
print(f"not has_license: {not has_license}")

# 组合使用逻辑运算符
temperature = 25
is_sunny = True
have_umbrella = True

# 复杂逻辑判断：温度适宜且（晴天或有雨伞）
good_weather = temperature > 20 and (is_sunny or have_umbrella)
print(f"适合出门: {good_weather}")  # True

# 逻辑运算符的短路特性
print("\n=== 短路特性演示 ===")
# and的短路：如果第一个条件为False，不会计算第二个条件
result1 = False and print("这句不会执行")  # print不会被执行
print(f"短路and结果: {result1}")

# or的短路：如果第一个条件为True，不会计算第二个条件
result2 = True or print("这句也不会执行")  # print不会被执行
print(f"短路or结果: {result2}")

# 逻辑运算符的优先级：not > and > or
a = True
b = False
c = True

# 不使用括号的情况下，运算顺序是：not b -> a and (not b) -> (a and (not b)) or c
result3 = a and not b or c
print(f"优先级示例: a and not b or c = {result3}")  # True

# 使用括号明确优先级
result4 = a and (not b) or c
result5 = a and not (b or c)
print(f"明确优先级1: a and (not b) or c = {result4}")     # True
print(f"明确优先级2: a and not (b or c) = {result5}")     # False

# 实际应用示例：用户权限检查
user_age = 20
is_member = True
is_vip = False
has_permission = False

# 检查是否可以访问内容：年满18岁且（是会员或VIP或有特殊权限）
can_access = user_age >= 18 and (is_member or is_vip or has_permission)
print(f"\n用户是否可以访问: {can_access}")  # True

# 布尔值的真假性
print("\n=== 各种值的真假性 ===")
print(f"bool(0): {bool(0)}")           # False
print(f"bool(1): {bool(1)}")           # True
print(f"bool(''): {bool('')}")         # False，空字符串
print(f"bool('hello'): {bool('hello')}")  # True，非空字符串
print(f"bool([]): {bool([])}")         # False，空列表
print(f"bool([1,2]): {bool([1,2])}")   # True，非空列表
print(f"bool(None): {bool(None)}")     # False，None值

# 赋值运算符
print("\n=== 赋值运算符 ===")

# 1. 基本赋值运算符 =
a = 10
print(f"基本赋值: a = {a}")

# 2. 加法赋值运算符 +=
a += 5  # 等价于 a = a + 5
print(f"加法赋值 a += 5: a = {a}")

# 3. 减法赋值运算符 -=
a -= 3  # 等价于 a = a - 3
print(f"减法赋值 a -= 3: a = {a}")

# 4. 乘法赋值运算符 *=
a *= 2  # 等价于 a = a * 2
print(f"乘法赋值 a *= 2: a = {a}")

# 5. 除法赋值运算符 /=
a /= 4  # 等价于 a = a / 4
print(f"除法赋值 a /= 4: a = {a}")

# 6. 整除赋值运算符 //=
b = 17
b //= 5  # 等价于 b = b // 5
print(f"整除赋值 b //= 5: b = {b}")

# 7. 取模赋值运算符 %=
c = 17
c %= 5  # 等价于 c = c % 5
print(f"取模赋值 c %= 5: c = {c}")

# 8. 幂运算赋值运算符 **=
d = 3
d **= 3  # 等价于 d = d ** 3
print(f"幂运算赋值 d **= 3: d = {d}")

# 字符串的赋值运算符应用
text = "Hello"
text += " World"  # 字符串拼接
print(f"字符串加法赋值: text = '{text}'")

text *= 2  # 字符串重复
print(f"字符串乘法赋值: text = '{text}'")

# 列表的赋值运算符应用
numbers = [1, 2, 3]
numbers += [4, 5]  # 列表扩展
print(f"列表加法赋值: numbers = {numbers}")

numbers *= 2  # 列表重复
print(f"列表乘法赋值: numbers = {numbers}")

# 多重赋值
x = y = z = 10
print(f"多重赋值: x = {x}, y = {y}, z = {z}")

# 交换赋值（Python特有的简洁写法）
x, y = 5, 15
print(f"交换前: x = {x}, y = {y}")
x, y = y, x  # 交换x和y的值
print(f"交换后: x = {x}, y = {y}")

# 解包赋值
coordinates = (10, 20, 30)
x, y, z = coordinates  # 将元组解包赋值给多个变量
print(f"解包赋值: x = {x}, y = {y}, z = {z}")

# 三元运算符（条件表达式）
# 语法：变量 = 值1 if 条件 else 值2
# 如果条件为True，返回值1；如果条件为False，返回值2

# 基本示例
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(f"年龄{age}岁，身份：{status}")

# 数值比较示例
a = 10
b = 20
max_value = a if a > b else b
print(f"a={a}, b={b}, 最大值：{max_value}")

# 与传统if-else对比
score = 85
# 传统写法
if score >= 60:
    result = "及格"
else:
    result = "不及格"
print(f"传统写法 - 分数{score}：{result}")

# 三元运算符写法
result = "及格" if score >= 60 else "不及格"
print(f"三元运算符 - 分数{score}：{result}")

# 嵌套三元运算符（不推荐，影响可读性）
score = 85
grade = "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"
print(f"嵌套三元运算符 - 分数{score}：{grade}")

# 在函数调用中使用


def get_absolute_value(x):
    return x if x >= 0 else -x


print(f"绝对值示例：|{-5}| = {get_absolute_value(-5)}")
print(f"绝对值示例：|{3}| = {get_absolute_value(3)}")

# 在列表推导式中使用
numbers = [-2, -1, 0, 1, 2]
processed = [x if x >= 0 else 0 for x in numbers]
print(f"列表推导式中的三元运算符：{numbers} -> {processed}")


# 位运算符
# 位运算符用于对二进制位进行操作

print("=== 位运算符详解 ===")

# 1. 按位与运算符 (&)
# 公式：两个二进制位都为1时，结果为1；否则为0
# 真值表：1&1=1, 1&0=0, 0&1=0, 0&0=0
a = 12  # 二进制：1100
b = 8   # 二进制：1000
result = a & b  # 结果：1000 = 8
print(f"{a} & {b} = {result}")  # 12 & 8 = 8
print(f"二进制：{bin(a)} & {bin(b)} = {bin(result)}")

# 2. 按位或运算符 (|)
# 公式：两个二进制位有一个为1时，结果为1；都为0时结果为0
# 真值表：1|1=1, 1|0=1, 0|1=1, 0|0=0
result = a | b  # 结果：1100 = 12
print(f"{a} | {b} = {result}")  # 12 | 8 = 12
print(f"二进制：{bin(a)} | {bin(b)} = {bin(result)}")

# 3. 按位异或运算符 (^)
# 公式：两个二进制位不同时，结果为1；相同时结果为0
# 真值表：1^1=0, 1^0=1, 0^1=1, 0^0=0
result = a ^ b  # 结果：0100 = 4
print(f"{a} ^ {b} = {result}")  # 12 ^ 8 = 4
print(f"二进制：{bin(a)} ^ {bin(b)} = {bin(result)}")

# 4. 按位取反运算符 (~)
# 公式：对每个二进制位取反，0变1，1变0
# 注意：Python中使用补码表示，~x = -(x+1)
x = 5  # 二进制：0101
result = ~x  # 结果：-6
print(f"~{x} = {result}")  # ~5 = -6
print(f"二进制：~{bin(x)} = {bin(result & 0xFFFFFFFF)}")  # 显示32位补码

# 5. 左移运算符 (<<)
# 公式：符号位不变，将二进制位向左移动n位，右边补0
# 等价于：x << n = x * (2^n)
x = 5  # 二进制：101
n = 2
result = x << n  # 结果：10100 = 20
print(f"{x} << {n} = {result}")  # 5 << 2 = 20
print(f"二进制：{bin(x)} << {n} = {bin(result)}")
print(f"公式验证：{x} * 2^{n} = {x * (2**n)}")

# 6. 右移运算符 (>>)
# 公式：符号位不变，将二进制位向右移动n位，左边补符号位
# 等价于：x >> n = x // (2^n)
x = 20  # 二进制：10100
n = 2
result = x >> n  # 结果：101 = 5
print(f"{x} >> {n} = {result}")  # 20 >> 2 = 5
print(f"二进制：{bin(x)} >> {n} = {bin(result)}")
print(f"公式验证：{x} // 2^{n} = {x // (2**n)}")

# 成员运算符
# 用于判断某个值是否存在于序列（字符串、列表、元组等）中
# in - 如果在指定的序列中找到值返回True，否则返回False
# not in - 如果在指定的序列中没有找到值返回True，否则返回False

print("=== 成员运算符示例 ===")

# 1. 在字符串中使用成员运算符
text = "Hello Python"
print(f"字符串：'{text}'")
print(f"'Python' in text: {'Python' in text}")  # True
print(f"'Java' in text: {'Java' in text}")      # False
print(f"'Python' not in text: {'Python' not in text}")  # False
print(f"'Java' not in text: {'Java' not in text}")      # True

# 2. 在列表中使用成员运算符
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
print(f"\n水果列表：{fruits}")
print(f"'苹果' in fruits: {'苹果' in fruits}")      # True
print(f"'西瓜' in fruits: {'西瓜' in fruits}")      # False
print(f"'西瓜' not in fruits: {'西瓜' not in fruits}")  # True

# 3. 在元组中使用成员运算符
numbers = (1, 2, 3, 4, 5)
print(f"\n数字元组：{numbers}")
print(f"3 in numbers: {3 in numbers}")          # True
print(f"6 in numbers: {6 in numbers}")          # False
print(f"6 not in numbers: {6 not in numbers}")  # True

# 4. 在字典中使用成员运算符（检查键）
student = {"姓名": "张三", "年龄": 20, "专业": "计算机科学"}
print(f"\n学生字典：{student}")
print(f"'姓名' in student: {'姓名' in student}")      # True
print(f"'性别' in student: {'性别' in student}")      # False
print(f"'性别' not in student: {'性别' not in student}")  # True

# 5. 在集合中使用成员运算符
colors = {"红色", "绿色", "蓝色"}
print(f"\n颜色集合：{colors}")
print(f"'红色' in colors: {'红色' in colors}")      # True
print(f"'黄色' in colors: {'黄色' in colors}")      # False

# 6. 实际应用示例 - 用户权限检查
admin_users = ["admin", "manager", "supervisor"]
current_user = "admin"
print(f"\n权限检查示例：")
print(f"当前用户：{current_user}")
if current_user in admin_users:
    print("用户具有管理员权限")
else:
    print("用户没有管理员权限")

# 7. 实际应用示例 - 输入验证
valid_options = ["是", "否", "y", "n", "yes", "no"]
user_input = "是"
print(f"\n输入验证示例：")
print(f"用户输入：{user_input}")
if user_input.lower() in [option.lower() for option in valid_options]:
    print("输入有效")
else:
    print("输入无效，请重新输入")

# 8. 子字符串检查
email = "user@example.com"
print(f"\n邮箱验证示例：")
print(f"邮箱：{email}")
if "@" in email and "." in email:
    print("邮箱格式可能正确")
else:
    print("邮箱格式不正确")

# 运算符优先级，从高到低 算术运算符 > 位运算符 > 比较运算符 > 逻辑运算符 > 赋值运算符 > 成员运算符 > 身份运算符
# 1. () 括号 - 最高优先级
# 2. ** 幂运算
# 3. +x, -x, ~x 一元运算符（正号、负号、按位取反）
# 4. *, /, //, % 乘法、除法、整除、取模
# 5. +, - 加法、减法
# 6. <<, >> 位移运算符
# 7. & 按位与
# 8. ^ 按位异或
# 9. | 按位或
# 10. ==, !=, <, >, <=, >=, is, is not, in, not in 比较运算符
# 11. not 逻辑非
# 12. and 逻辑与
# 13. or 逻辑或
# 14. if-else 三元运算符
# 15. lambda 匿名函数 - 最低优先级
