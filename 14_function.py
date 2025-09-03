
# 函数详解

# 1. 函数定义
# 语法：
# def 函数名(参数):
#     代码块
#
# 例子：定义一个简单的问候函数
import math


def greet():
    print("你好，欢迎学习Python！")

# 例子：定义一个带参数的函数


def greet_person(name):
    print(f"你好，{name}！")

# 2. 函数调用
# 语法：
# 函数名(参数)
#
# 函数调用机制：
# 1. 调用函数时，会创建一个栈帧（stack frame）
# 2. 栈帧中包含函数的局部变量和参数
# 3. 函数执行完后，栈帧被销毁
# 4. 如果函数有返回值，则返回值会被存储在栈帧中
# 5. 如果函数有参数，则参数会被存储在栈帧中
# 6. 如果函数有局部变量，则局部变量会被存储在栈帧中


# 例子：调用函数
greet()  # 输出：你好，欢迎学习Python！
greet_person("小明")  # 输出：你好，小明！

# 如果同一个文件，出现两个函数名相同的函数，则以就近原则调用


def test_function():
    print("第一个函数")


def test_function():
    print("第二个函数")


test_function()  # 输出：第二个函数

# 调用另外一个文件中的函数，需要导入模块
# from 模块名 import 函数名
# 调用函数时，需要使用模块名.函数名
# 模块名.函数名()
# 也可以使用别名，别名.函数名()
# 别名 = 模块名
# 别名.函数名()

# 例子：导入math模块并使用
result = math.sqrt(16)  # 计算平方根
print(f"16的平方根是：{result}")

# 3. 函数参数
# 3.1 位置参数


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)  # 位置参数：3传给a，5传给b
print(f"3 + 5 = {result}")

# 3.2 关键字参数
# 也可以位置参数和关键字参数混合使用，但位置参数必须在关键字参数之前


def introduce(name, age, city):
    print(f"我叫{name}，今年{age}岁，来自{city}")


# 使用关键字参数
introduce(name="小红", age=20, city="北京")
# 混合使用
introduce("小李", age=25, city="上海")

# 支持默认参数/缺省参数，缺省参数必须放在位置参数之后，且缺省参数必须放在参数列表的最后


def greet_with_default(name, greeting="你好"):
    print(f"{greeting}，{name}！")


greet_with_default("小王")  # 使用默认值：你好，小王！
greet_with_default("小张", "早上好")  # 传入自定义值：早上好，小张！

# 支持可变参数/不定长参数，可变参数必须放在参数列表的最后
# 可变参数/不定长参数：*args，*args表示可变参数，args是一个元组，可以接收多个参数


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(f"求和结果：{sum_all(1, 2, 3, 4, 5)}")  # 输出：15

# 可变关键字参数：**kwargs，kwargs是一个字典，可以接收多个关键字参数


def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="小刘", age=22, hobby="编程")

# 4. 函数返回值
# 4.1 返回一个值


def multiply(a, b):
    return a * b


result = multiply(4, 6)
print(f"4 × 6 = {result}")

# 4.2 返回多个值


def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result


sum_val, diff_val = calculate(10, 3)
print(f"和：{sum_val}，差：{diff_val}")

# 4.3 返回None


def print_message(msg):
    print(msg)
    # 没有return语句，默认返回None


result = print_message("这是一个消息")
print(f"函数返回值：{result}")  # 输出：None

# 函数的传参机制（重点）：
# 1. 字符串和数值型
# 字符串和数值型是不可变类型，传参时，对应的变量的值发生了变化时，它对应的内存地址也发生了变化


def change_number(x):
    x = 100
    print(f"函数内部 x = {x}")


num = 50
print(f"调用前 num = {num}")
change_number(num)
print(f"调用后 num = {num}")  # num仍然是50，没有被改变

# 2. 列表和字典
# 列表和字典是可变类型，传参时，对应的变量的值发生了变化时，它对应的内存地址没有变化


def change_list(lst):
    lst.append(4)
    print(f"函数内部列表：{lst}")


my_list = [1, 2, 3]
print(f"调用前列表：{my_list}")
change_list(my_list)
print(f"调用后列表：{my_list}")  # 列表被改变了

# 递归机制：
# 递归是一种函数调用自身的方式，递归可以用于解决一些复杂的问题，如斐波那契数列、阶乘等
# 递归的原理：
# 1. 递归函数必须有一个结束条件，否则会无限递归
# 递归的重要规则：
# 1. 执行一个函数时，会创建一个新的栈帧
# 2. 函数的变量是独立的，不是全局变量
# 3. 递归函数必须有一个结束条件，也就是必须向退出递归的条件逼近，否则会无限递归
# 4. 当一个函数执行完毕，或者遇到return，那么该函数执行完毕，也会返回结果，遵守谁调用，就将结果返回给谁，同时该函数执行完毕

# 例子：计算阶乘


def factorial(n):
    if n == 0 or n == 1:  # 结束条件
        return 1
    else:
        return n * factorial(n - 1)  # 递归调用


print(f"5的阶乘是：{factorial(5)}")  # 输出：120

# 例子：斐波那契数列


def fibonacci(n):
    if n <= 1:  # 结束条件
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # 递归调用


print(f"斐波那契数列第6项：{fibonacci(6)}")  # 输出：8

# 函数作为参数传递：
# 1. 函数作为参数传递，可以传递一个函数名，也可以传递一个匿名函数


def apply_operation(x, y, operation):
    return operation(x, y)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# 传递函数作为参数
result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)
print(f"5 + 3 = {result1}")  # 输出：8
print(f"5 × 3 = {result2}")  # 输出：15

# lambda匿名函数：
# 定义与基本语法： lambda 参数1,参数2,参数3: 表达式
# 示例：
# lambda x,y: x+y
# 调用：
# (lambda x,y: x+y)(1,2)
# 匿名函数与内置函数的结合使用
# 匿名函数与内置函数的结合使用：
# 函数体只能有一个表达式，不能有多个表达式，表达式的结果就是返回值，只能写一行

# 例子：简单的lambda函数


def square(x): return x ** 2


print(f"5的平方是：{square(5)}")  # 输出：25

# 例子：使用lambda与内置函数
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"平方后的列表：{squared_numbers}")

# 例子：使用lambda与filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表：{even_numbers}")

# 全局变量和局部变量：
# 全局变量：在函数外部定义的变量
# 局部变量：在函数内部定义的变量
# 全局变量和局部变量是独立的，不是同一个变量
# 全局变量和局部变量可以同名，但局部变量会覆盖全局变量
# 可以使用global关键字声明全局变量，声明之后，该变量就是全局变量，可以被函数内部修改

# 例子：全局变量和局部变量
global_var = "我是全局变量"


def test_scope():
    local_var = "我是局部变量"
    print(f"函数内部：{global_var}")
    print(f"函数内部：{local_var}")


test_scope()
print(f"函数外部：{global_var}")
# print(f"函数外部：{local_var}")  # 这行会报错，因为local_var是局部变量

# 例子：使用global关键字
counter = 0


def increment():
    global counter  # 声明使用全局变量
    counter += 1
    print(f"计数器值：{counter}")


increment()  # 输出：1
increment()  # 输出：2
print(f"全局计数器：{counter}")  # 输出：2

# 例子：局部变量覆盖全局变量
message = "全局消息"


def show_message():
    message = "局部消息"  # 局部变量覆盖全局变量
    print(f"函数内部：{message}")


show_message()  # 输出：局部消息
print(f"函数外部：{message}")  # 输出：全局消息
