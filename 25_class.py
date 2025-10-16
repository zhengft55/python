# oop快速入门
# 1. 定义类
# 语法：
# class 类名:
#     类属性
#     类方法
#
# 例子：定义一个学生类
class Student:
    name = None  # 类属性
    # 是的，这里通过构造器（__init__方法）来动态设置类的属性

    def __init__(self, name, age):
        # 这里的self.name与第十行的name并不是同一个变量
        # 第十行的name是类属性，self.name是实例属性
        # 这里是将传入的参数name赋值给实例的name属性
        self.name = name  # 实例属性
    # 这里可以在创建对象时将传入的参数动态赋值给属性
        self.age = age

    # 成员方法的定义语法：
    # 语法：
    # def 方法名(self, 参数):
    #     方法体
    #
    # self是成员方法的第一个参数，代表的是对象本身，在成员方法中，可以使用self来访问对象的属性和方法
    # 例子：定义一个学习方法
    def study(self):
        print(f"{self.name}正在学习")


# 2. 创建对象
student = Student("张三", 20)

# 3. 调用方法
student.study()

print(student.name)
student1 = student
student1.name = "李四"
print(student.name)
student1 = None
print(student.name)
# print(student1.name)


def demo():
    print("demo")


student1 = Student("张三1", 20)
student.demo1 = demo
student.demo1()
# student1.demo1()


# self参数的传递
# self通常是必须写的，self传入的是对象本身，哪个对象调用，self就代表哪个对象
# 如果不写，则需要使用@staticmethod装饰器来装饰方法，变为静态
# 静态方法不需要传入self参数，可以直接使用类名调用
# 由于静态方法没有self参数，所以无法访问对象的属性和方法，只能访问类的属性和方法
# 静态方法可以被类和对象调用
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃")

    @staticmethod
    def demo2():
        print("demo2")


dog = Dog("旺财", 3)
dog.eat()
dog.demo2()
Dog.demo2()


# 对象作为参数的传参机制  地址引用，传地址不传值

# 构造方法
# def __init__ (self, 形参列表)：
# 创建对象时，自动执行__init__ 方法
# 不能有返回值
# 即使写了多个 也只有最后一个会生效
# 若要实现多个构造方法：① 可变长度参数 *args
# ②：classmethod重载
