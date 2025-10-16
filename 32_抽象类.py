# 抽象类（Abstract Class）是一种只能被继承，不能被实例化的类。它用于作为其他类的通用模板，强制子类必须实现某些方法，适用于需要定义规范/接口而不关心具体实现的场景。
# 抽象类主要用来约定和规范，不能直接创建对象。

# 在Python中抽象类需要用abc模块，通过@abstractmethod来标记抽象方法。
from abc import ABC, abstractmethod

# 示例：定义一个抽象的“动物”类，约定所有动物都要能“发声”


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # 抽象方法无具体实现，子类必须重写

    @abstractmethod
    def eat(self):
        pass  # 抽象方法无具体实现，子类必须重写

    # 抽象类中可以有普通方法
    def hi(self):
        pass

# 不能直接实例化抽象类
# a = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract method speak

# 正确做法：继承抽象类并实现抽象方法


class Dog(Animal):
    def speak(self):
        print("汪汪!")

    def eat(self):
        print("汪汪!")


class Cat(Animal):
    def speak(self):
        print("喵喵!")

    def eat(self):
        print("汪汪!")


dog = Dog()
cat = Cat()
dog.speak()  # 输出: 汪汪!
cat.speak()  # 输出: 喵喵!

# 常见用途：需要统一接口/规范，但不同子类实现细节不同（如各种交通工具计算价格、各种图形计算面积等）
