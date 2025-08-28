# 标识符命名规则
# 标识符是用来标识变量、函数、类、模块等对象的名称
# 在Python中，标识符必须遵循一定的命名规则

import keyword
print("=== 1. 标识符的基本规则 ===")
# 规则1：只能包含字母（a-z, A-Z）、数字（0-9）和下划线（_）
valid_name = "有效的标识符"
valid_name2 = "也是有效的"
_private_var = "以下划线开头"
variable123 = "包含数字"
print(f"有效标识符示例：{valid_name}, {_private_var}, {variable123}")

# 规则2：不能以数字开头
# 123invalid = "错误！不能以数字开头"  # 这行会报错，所以注释掉
name1 = "正确，数字可以在中间或结尾"
print(f"正确的数字使用：{name1}")

# 规则3：不能包含空格
# user name = "错误！不能包含空格"  # 这行会报错，所以注释掉
user_name = "正确，用下划线代替空格"
print(f"正确的空格处理：{user_name}")

# 规则4：区分大小写
Name = "大写N开头"
name = "小写n开头"
NAME = "全大写"
print(f"大小写敏感：Name='{Name}', name='{name}', NAME='{NAME}'")

print("\n=== 2. 不能使用的标识符（保留字） ===")
# Python的保留字（关键字）不能用作标识符
print("Python的所有保留字：")
print(keyword.kwlist)
print(f"保留字总数：{len(keyword.kwlist)}")

# 常见保留字示例
# if = 10      # 错误！if是保留字
# for = 20     # 错误！for是保留字
# class = 30   # 错误！class是保留字

print("\n=== 3. 无效标识符示例 ===")
print("以下是无效的标识符示例（不能在代码中使用）：")
print("1. 以数字开头：❌ 2nd_place, 123abc, 9name")
print("2. 包含空格：❌ user name, my variable, first name")
print("3. 包含特殊字符：❌ user-name, email@domain, price$")
print("4. 使用保留字：❌ if, for, class, def, import")
print("5. 空标识符：❌ 空字符串")

print("\n=== 4. 标识符命名约定（PEP 8风格指南） ===")

# 4.1 变量和函数名：使用小写字母，单词间用下划线分隔
# 私有函数：以单个下划线开头（约定俗成，表示内部使用）


def _private_function():
    """这是一个私有函数，通常只在类或模块内部使用"""
    return "这是私有函数"

# 特殊方法：以双下划线开头和结尾（如 __init__, __str__ 等）


class ExampleClass:
    def __init__(self, value):
        """构造函数，创建对象时自动调用"""
        self.value = value

    def __str__(self):
        """字符串表示方法，当使用print()时自动调用"""
        return f"ExampleClass对象，值为：{self.value}"

    def __len__(self):
        """长度方法，当使用len()函数时自动调用"""
        return len(str(self.value))


# 演示特殊方法的使用
example = ExampleClass("Hello World")
print(f"对象的字符串表示: {example}")        # 自动调用 __str__ 方法
print(f"对象的长度: {len(example)}")         # 自动调用 __len__ 方法


user_name = "张三"
user_age = 25
total_score = 95.5
first_name = "张"
last_name = "三"


def calculate_average(scores):
    """计算平均分的函数"""
    return sum(scores) / len(scores)


print(f"变量命名示例：{user_name}, {user_age}, {total_score}")
print(f"多单词变量：{first_name}, {last_name}")

# 4.2 常量：使用全大写字母，单词间用下划线分隔
MAX_SIZE = 100
PI = 3.14159
DEFAULT_TIMEOUT = 30
MAX_RETRY_COUNT = 5
print(f"常量命名示例：MAX_SIZE={MAX_SIZE}, PI={PI}")

# 4.3 类名：使用驼峰命名法（每个单词首字母大写）


class StudentInfo:
    """学生信息类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class DatabaseConnection:
    """数据库连接类"""
    pass


class UserAccountManager:
    """用户账户管理类"""
    pass


print("类名示例：StudentInfo, DatabaseConnection, UserAccountManager")

# 4.4 私有变量：以单个下划线开头（约定俗成，表示内部使用）


class MyClass:
    def __init__(self):
        self.public_var = "公共变量"
        self._private_var = "私有变量（约定）"
        self.__very_private = "强私有变量"


obj = MyClass()
print(f"公共变量：{obj.public_var}")
print(f"私有变量：{obj._private_var}")

print("\n=== 5. 特殊标识符 ===")
# 5.1 以双下划线开头和结尾的标识符（魔术方法）


class ExampleClass:
    def __init__(self):
        self.value = 42

    def __str__(self):
        return f"ExampleClass(value={self.value})"

    def __len__(self):
        return self.value


example = ExampleClass()
print(f"魔术方法示例：{example}")
print(f"__len__方法：{len(example)}")

# 名称改写：以双下划线开头但不以双下划线结尾（会被Python解释器改写）


class ParentClass:
    def __init__(self):
        self.public_var = "公共变量"          # 公共变量
        self._protected_var = "受保护变量"     # 受保护变量（约定）
        self.__private_var = "私有变量"       # 私有变量（名称会被改写）

    def show_variables(self):
        print(f"公共变量: {self.public_var}")
        print(f"受保护变量: {self._protected_var}")
        print(f"私有变量: {self.__private_var}")


# 演示名称改写机制
print("=== 名称改写演示 ===")
obj = ParentClass()
obj.show_variables()
print(f"直接访问公共变量: {obj.public_var}")
print(f"直接访问受保护变量: {obj._protected_var}")
# print(f"直接访问私有变量: {obj.__private_var}")  # 这行会报错！
print(f"通过改写后的名称访问私有变量: {obj._ParentClass__private_var}")  # 实际的内部名称

# 5.2 单下划线 _ 作为临时变量或忽略的变量
for _ in range(3):
    print("使用_作为不需要的变量")

# 在元组解包中忽略不需要的值
coordinates = (10, 20, 30)
x, _, z = coordinates  # 忽略y坐标
print(f"解包示例：x={x}, z={z}")

print("\n=== 6. 中文标识符（Python 3支持Unicode） ===")
# Python 3支持Unicode字符作为标识符，但不能包含空格
姓名 = "李四"
年龄 = 30
成绩 = [85, 90, 78]
平均分 = sum(成绩) / len(成绩)
学生姓名 = "王五"  # 正确：中文字符连在一起
# 学生 姓名 = "赵六"  # 错误：中文之间有空格


def 计算总分(分数列表):
    """计算总分的函数"""
    return sum(分数列表)


print(f"中文标识符示例：{姓名}，年龄{年龄}岁，平均分{平均分:.1f}")
print(f"总分：{计算总分(成绩)}")
print(f"多字中文标识符：{学生姓名}")

print("\n=== 7. 标识符命名最佳实践 ===")
# 7.1 使用有意义的名称，单词间用下划线连接
good_examples = {
    "user_count": 150,              # 清晰表达含义
    "is_valid": True,               # 布尔变量用is_开头
    "has_permission": False,        # 或者用has_开头
    "max_retry_times": 3,           # 具体描述用途
    "student_grade_list": [85, 90],  # 描述性的列表名
    "database_connection_url": "localhost",  # 长但清晰的名称
}

# 7.2 避免使用容易混淆的字符
# 避免使用：l（小写L）、O（大写O）、I（大写i）等容易和数字混淆的字符
count_items = 10    # 而不是 l = 10
is_open = True      # 而不是 O = True
item_id = "001"     # 而不是 I = "001"

print("命名最佳实践示例：")
for key, value in good_examples.items():
    print(f"  {key}: {value}")

print("\n=== 8. 空格相关的错误示例 ===")
print("包含空格的错误标识符示例：")
print("❌ user name = 'John'     # 变量名不能有空格")
print("❌ first name = 'Jane'    # 变量名不能有空格")
print("❌ my list = [1, 2, 3]    # 变量名不能有空格")
print("❌ data base = 'mysql'    # 变量名不能有空格")
print("")
print("正确的替代方案：")
print("✅ user_name = 'John'     # 用下划线代替空格")
print("✅ first_name = 'Jane'    # 用下划线代替空格")
print("✅ my_list = [1, 2, 3]    # 用下划线代替空格")
print("✅ database = 'mysql'     # 合并为一个词或用下划线")

print("\n=== 9. 检查标识符是否有效 ===")


def check_identifier(name):
    """检查给定字符串是否是有效的Python标识符"""
    if name.isidentifier():
        if keyword.iskeyword(name):
            return f"'{name}' 是有效标识符但是保留字，不能使用"
        else:
            return f"'{name}' 是有效的标识符"
    else:
        return f"'{name}' 不是有效的标识符"


# 测试各种标识符，特别包含空格的情况
test_names = [
    "valid_name",       # 有效
    "2invalid",         # 无效：以数字开头
    "user name",        # 无效：包含空格
    "user-name",        # 无效：包含连字符
    "class",            # 有效但是保留字
    "_private",         # 有效
    "中文变量",          # 有效
    "name123",          # 有效
    "",                 # 无效：空字符串
    "hello world",      # 无效：包含空格
    "my variable",      # 无效：包含空格
    "first_name",       # 有效：用下划线代替空格
]

print("标识符有效性检查：")
for name in test_names:
    print(f"  {check_identifier(name)}")

print("\n=== 总结 ===")
print("Python标识符命名要点：")
print("1. 只能包含字母、数字、下划线，不能以数字开头")
print("2. 不能包含空格或其他特殊字符")
print("3. 区分大小写")
print("4. 不能使用保留字")
print("5. 遵循PEP 8命名约定")
print("6. 使用有意义的名称，提高代码可读性")
print("7. 支持Unicode字符，可以使用中文等非ASCII字符")
print("8. 多个单词用下划线连接，而不是空格")


# 关键字一览
print("\n=== Python关键字（保留字）一览 ===")
print("以下是Python中的所有关键字，不能用作标识符：")

# 导入keyword模块来获取所有关键字

# 获取所有关键字列表
all_keywords = keyword.kwlist
print(f"Python {keyword.__name__} 模块识别的关键字总数：{len(all_keywords)}")

# 按类别展示关键字
print("\n分类展示：")

# 1. 控制流关键字
control_flow = ['if', 'elif', 'else', 'for',
                'while', 'break', 'continue', 'pass']
print(f"控制流关键字：{[kw for kw in control_flow if kw in all_keywords]}")

# 2. 逻辑关键字
logical = ['and', 'or', 'not', 'is', 'in']
print(f"逻辑关键字：{[kw for kw in logical if kw in all_keywords]}")

# 3. 函数和类关键字
func_class = ['def', 'class', 'return', 'yield', 'lambda']
print(f"函数和类关键字：{[kw for kw in func_class if kw in all_keywords]}")

# 4. 异常处理关键字
exception = ['try', 'except', 'finally', 'raise', 'assert']
print(f"异常处理关键字：{[kw for kw in exception if kw in all_keywords]}")

# 5. 导入关键字
import_kw = ['import', 'from', 'as']
print(f"导入关键字：{[kw for kw in import_kw if kw in all_keywords]}")

# 6. 特殊值关键字
special_values = ['True', 'False', 'None']
print(f"特殊值关键字：{[kw for kw in special_values if kw in all_keywords]}")

# 7. 其他关键字
other_keywords = ['global', 'nonlocal', 'del', 'with', 'async', 'await']
print(f"其他关键字：{[kw for kw in other_keywords if kw in all_keywords]}")

# 完整列表（按字母顺序）
print(f"\n完整关键字列表（按字母顺序）：")
sorted_keywords = sorted(all_keywords)
for i, kw in enumerate(sorted_keywords, 1):
    print(f"{i:2d}. {kw:8s}", end="")
    if i % 4 == 0:  # 每行显示4个关键字
        print()
if len(sorted_keywords) % 4 != 0:
    print()

print("\n注意事项：")
print("• 这些关键字不能用作变量名、函数名或类名")
print("• 关键字区分大小写，例如 'True' 是关键字，但 'true' 不是")
print("• 可以使用 keyword.iskeyword('word') 来检查某个词是否为关键字")

# 演示检查关键字的方法
print(f"\n演示关键字检查：")
test_words = ['if', 'If', 'IF', 'class', 'Class', 'variable']
for word in test_words:
    is_keyword = keyword.iskeyword(word)
    print(f"keyword.iskeyword('{word}'): {is_keyword}")
