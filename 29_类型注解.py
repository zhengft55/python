# 类型注解（Type Hints）

# 类型注解（Type Hints）用于为变量、函数参数和返回值指定类型，使代码更加清晰、易于理解和维护。
# 仅为提示性，并不是强制性的， 检测出警告，仍然可以运行
# 示例1：变量注解
from typing import Union
name: str = "小明"
age: int = 18
scores: list[float] = [95.5, 88.0, 72.5]
dict1: dict[str, int] = {"s": 1}


class Cat:
    def __init__(self) -> None:
        pass


# 实例类型注解
cat: Cat = Cat()

# 注释中使用注解    已被弃用
N1 = "20"  # type:  dict


# 示例2：函数参数和返回值注解


def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."


result = greet("小明", 18)

# 示例3：类属性和方法注解


class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def study(self, subject: str) -> None:
        print(f"{self.name} 正在学习 {subject}")

# 使用第三方工具mypy可以进行类型检查：mypy 文件名.py


# Union 类型注解
# 当一个值可以有多种类型时，可以使用 Union 进行类型注解。
# 语法：Union[类型1, 类型2, ...]
# 需要从 typing 模块导入 Union


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


a: Union[int, str] = 10
b: Union[int, str] = "hello"

print(add(2, 3.5))      # 输出：5.5
print(add(1, 2))        # 输出：3

# 也可使用 | （Python 3.10+ 语法糖）：


def print_value(val: int | str) -> None:
    print(f"值为: {val}")


print_value(123)
print_value("abc")
