# 程序控制结构
# 1. 顺序结构
# 2. 分支结构
# 3. 循环结构

# 1.单分支结构
# 语法：
# if 条件:
#     代码块
#
# 例子：判断成绩是否及格
import random
score = 85
if score >= 60:
    print("恭喜你，成绩及格了！")

# 2.双分支结构
# 语法：
# if 条件:
#     代码块
# else:
#     代码块
#
# 例子：判断奇偶数
num = 7
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 3.多分支结构
# 语法：
# if 条件:
#     代码块
# elif 条件:
#     代码块
# else:
#     代码块

# 例子：根据成绩给出等级
score = 88
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 4. 嵌套分支结构
# 语法：
# if 条件:
#     代码块
#     if 条件:
#         代码块
#     else:
#         代码块
# else:
#     代码块

# 例子：判断年龄和性别
age = 25
gender = "男"
if age >= 18:
    print("成年人")
    if gender == "男":
        print("成年男性")
    else:
        print("成年女性")
else:
    print("未成年人")

# 5. for循环结构
# 语法：
# for 变量 in 序列:
#     代码块
#
# 例子1：遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 例子2：使用range函数
for i in range(5):  # 打印0到4
    print(f"第{i+1}次循环")

# for可以与else搭配使用，当for循环正常执行完，没有被break中断，则执行else语句
# 语法：
# for 变量 in 序列:
#     代码块
# else:
#     代码块

# 例子：查找特定元素
numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print(f"找到了{target}")
        break
else:
    print(f"没有找到{target}")

# 6. while循环结构
# 语法：
# while 条件:
#     代码块

# 例子：计算1到10的和
sum_result = 0
i = 1
while i <= 10:
    sum_result += i
    i += 1
print(f"1到10的和是：{sum_result}")

# while可以与else搭配使用，当while循环正常执行完，没有被break中断，则执行else语句
# 语法：
# while 条件:
#     代码块
# else:
#     代码块

# 例子：猜数字游戏
secret_number = random.randint(1, 10)
guess_count = 0
max_guesses = 3

while guess_count < max_guesses:
    guess = int(input("请猜一个1-10之间的数字："))
    guess_count += 1

    if guess == secret_number:
        print("恭喜你猜对了！")
        break
    elif guess < secret_number:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"游戏结束，正确答案是{secret_number}")

# 7. 多重循环结构
# 语法：
# for 变量 in 序列:
#     for 变量 in 序列:
#         代码块
#
# 例子1：打印乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行

# 例子2：打印金字塔
rows = 5
for i in range(1, rows + 1):
    # 打印空格
    for j in range(rows - i):
        print(" ", end="")
    # 打印星号
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # 换行

# break: 跳出当前循环, 如果循环有可选的else，则不执行else
#        如果 for循环被break，该循环的控制变量会保持循环结束时的值
# 例子：找到第一个偶数就停止
numbers = [1, 3, 8, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"找到第一个偶数：{num}")
        break

# continue: 跳过当前循环，继续执行下一次循环
# 例子：只打印奇数
for i in range(10):
    if i % 2 == 0:  # 如果是偶数就跳过
        continue
    print(f"奇数：{i}")

# pass: 占位符，不执行任何操作
# 例子：暂时空着的函数或类


def future_function():
    pass  # 还没想好要写什么，先用pass占位

# return: 返回值，跳出当前函数
# 例子：计算两数之和的函数


def add_numbers(a, b):
    result = a + b
    return result  # 返回计算结果并退出函数

# yield: 生成器，返回一个迭代器
# 例子：生成斐波那契数列


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  # 返回当前值，但不结束函数
        a, b = b, a + b

# raise: 抛出异常
# 例子：自定义异常


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")  # 抛出异常
    return a / b

# assert: 断言
# 例子：确保输入是正数


def calculate_square_root(x):
    # assert断言语句详解：
    # 语法：assert 条件表达式, "错误信息"
    # 作用：在开发和调试阶段检查程序的正确性
    # 如果条件为True，程序继续执行
    # 如果条件为False，抛出AssertionError异常并显示错误信息
    #
    # 工作原理：
    # 1. 计算条件表达式 x >= 0 的值
    # 2. 如果结果为True，什么都不做，继续执行后面的代码
    # 3. 如果结果为False，抛出AssertionError("输入必须是非负数")
    #
    # 注意事项：
    # - assert主要用于调试，生产环境中可以通过-O参数禁用
    # - 不应该用assert来处理用户输入验证，应该用if语句和raise
    # - assert适合用来检查程序内部的逻辑错误
    assert x >= 0, "输入必须是非负数"  # 断言：确保x不是负数，否则抛出AssertionError
    return x ** 0.5


# with: 上下文管理器
# 例子：文件操作
with open("example.txt", "w") as file:
    file.write("Hello World")  # 文件会自动关闭

# try: 异常处理
# except: 异常处理
# finally: 异常处理
# 例子：处理可能出现的错误
try:
    result = 10 / 0  # 这里会出现除零错误
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生了其他错误：{e}")
finally:
    print("无论是否出错都会执行这里")
