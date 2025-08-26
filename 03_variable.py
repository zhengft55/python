# -*- coding: utf-8 -*-

# Python变量的三个基本要素详解

"""
变量的三个基本要素：
1. 类型（Type）：变量存储的数据类型
2. 名称（Name）：变量的标识符
3. 值（Value）：变量存储的具体数据
"""

# ===== 1. 变量类型示例 =====

# 整数类型（int）
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数类型（float）
height = 175.5
print(f"身高: {height}, 类型: {type(height)}")

# 字符串类型（str）
name = "张三"
print(f"姓名: {name}, 类型: {type(name)}")

# 布尔类型（bool）
is_student = True
print(f"是否为学生: {is_student}, 类型: {type(is_student)}")

# 列表类型（list）
hobbies = ["编程", "阅读", "运动"]
print(f"爱好: {hobbies}, 类型: {type(hobbies)}")

# 字典类型（dict）
person_info = {"姓名": "李四", "年龄": 30, "职业": "程序员"}
print(f"个人信息: {person_info}, 类型: {type(person_info)}")

print("\n" + "="*50 + "\n")

# ===== 2. 变量名称规范示例 =====

# ===== Python变量命名规范总结 =====

# 1. 推荐的命名规范（遵循PEP 8标准）
student_name = "王五"          # 蛇形命名法：使用下划线分隔的小写字母
total_score = 95              # 数字和字母组合：可以包含数字，但不能以数字开头
max_retry_count = 3           # 描述性命名：变量名应该清楚表达其用途

# 2. 常量命名规范
PI = 3.14159                  # 常量：使用全大写字母，多个单词用下划线分隔
MAX_FILE_SIZE = 1024          # 常量示例：文件大小限制
DEFAULT_TIMEOUT = 30          # 常量示例：默认超时时间

# 3. 私有变量命名规范
_private_var = "私有变量"      # 单下划线开头：表示内部使用的变量
__very_private = "很私有"      # 双下划线开头：表示类的私有属性（会触发名称修饰）

# 4. 其他有效但不推荐的命名方式
userName = "驼峰命名"          # 小驼峰命名法：在Python中不推荐，但语法有效
ClassName = "大驼峰命名"       # 大驼峰命名法：通常用于类名，不用于变量名

# 5. 特殊用途的命名
temp_file_path = "/tmp/data"   # 临时变量：使用temp_前缀
is_valid = True               # 布尔变量：使用is_、has_、can_等前缀
user_count = 10               # 计数变量：使用_count后缀

# 错误的变量命名示例（注释掉，因为会报错）
# 2name = "错误"               # 不能以数字开头
# class = "关键字"             # 不能使用Python关键字
# name-with-dash = "错误"      # 不能包含连字符（连字符是"-"符号，用于连接单词，但在Python变量名中不被允许）

print(f"学生姓名: {student_name}")
print(f"总分: {total_score}")
print(f"圆周率: {PI}")

print("\n" + "="*50 + "\n")

# ===== 3. 变量值的赋值和修改示例 =====

# 基本赋值
score = 80
print(f"初始分数: {score}")

# 重新赋值（变量值可以改变）
score = 95
print(f"修改后分数: {score}")

# 多重赋值
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 链式赋值
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# 交换变量值
num1, num2 = 10, 20
print(f"交换前: num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"交换后: num1={num1}, num2={num2}")

print("\n" + "="*50 + "\n")

# ===== 4. 动态类型示例 =====

# Python是动态类型语言，变量类型可以改变
variable = 42                 # 整数
print(f"值: {variable}, 类型: {type(variable)}")

variable = "现在是字符串"       # 字符串
print(f"值: {variable}, 类型: {type(variable)}")

variable = [1, 2, 3]          # 列表
print(f"值: {variable}, 类型: {type(variable)}")

print("\n" + "="*50 + "\n")

# ===== 5. 变量作用域示例 =====

# 全局变量
global_var = "我是全局变量"

def demo_function():
    # 局部变量
    local_var = "我是局部变量"
    print(f"函数内部 - 全局变量: {global_var}")
    print(f"函数内部 - 局部变量: {local_var}")

demo_function()
print(f"函数外部 - 全局变量: {global_var}")
# print(local_var)  # 这行会报错，因为local_var在函数外部不可访问

print("\n" + "="*50 + "\n")

# ===== 6. 变量内存地址示例 =====

# 查看变量在内存中的地址
text1 = "Hello"
text2 = "Hello"
text3 = text1

print(f"text1的值: {text1}, 内存地址: {id(text1)}")
print(f"text2的值: {text2}, 内存地址: {id(text2)}")
print(f"text3的值: {text3}, 内存地址: {id(text3)}")
print(f"text1和text2指向同一内存地址: {id(text1) == id(text2)}")

# 为什么text1和text2会指向同一地址？
print("\n解释:")
print("1. 字符串驻留机制（String Interning）:")
print("   - Python会自动缓存小的字符串和常见字符串")
print("   - 当创建相同内容的字符串时，Python会复用已存在的字符串对象")
print("   - 这样可以节省内存空间，提高性能")

print("\n2. text3 = text1 直接赋值:")
print("   - text3直接指向text1所指向的对象")
print("   - 这是引用赋值，不会创建新的字符串对象")

# 验证字符串驻留机制
print("\n验证字符串驻留机制:")
str_a = "Python"
str_b = "Python"
print(f"str_a和str_b内容相同但分别创建: {id(str_a) == id(str_b)}")

# 对比：创建新对象的情况
print("\n对比：强制创建新对象的情况:")
str_c = "Hello"
str_d = "".join(["H", "e", "l", "l", "o"])  # 动态创建字符串
print(f"str_c: {str_c}, 地址: {id(str_c)}")
print(f"str_d: {str_d}, 地址: {id(str_d)}")
print(f"内容相同但地址可能不同: {id(str_c) == id(str_d)}")

# 总结
print("\n" + "="*50)
print("变量三要素总结:")
print("1. 类型（Type）：决定变量能存储什么样的数据")
print("2. 名称（Name）：用于标识和访问变量的标识符")
print("3. 值（Value）：变量实际存储的数据内容")
print("="*50)
