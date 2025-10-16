# 继承
# 定义一个父类 Animal
from inspect import AGEN_CLOSED


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def speak(self):
        print(f"{self.name} 发出叫声")

    def get_age(self):
        return self.__age

# 定义一个子类 Dog，继承自 Animal


class Dog(Animal):

    age = None
    # def speak(self):
    #     print(f"{self.name} 汪汪叫")

    def eat(self):
        print(f"{self.name} 汪汪吃, 年龄{self.get_age()}  公共年龄{self.age}")


# 实例化
animal = Animal("动物", 20)
animal.speak()  # 输出：动物 发出叫声
# animal.eat()

dog = Dog("小狗", 21)
dog.speak()     # 输出：小狗 汪汪叫
dog.eat()
dog.age = 22
dog.eat()


# 子类继承父类的所有属性和方法，非私有的可以直接在子类访问，私有的需要通过父类的公共方法访问

# object是所有其他类的基类

# 支持多重继承 遵循MRO顺序
# 如果有同名的成员，遵循从左到右的优先级
class A:
    strc = 1

    def __init__(self, stra, **kwargs):
        print("A.__init__ start", kwargs)
        self.stra = stra
        super().__init__(**kwargs)
        print("A.__init__ end")


class B:
    strc = 2

    def __init__(self, strb, **kwargs):
        print("B.__init__ start", kwargs)
        self.strb = strb
        super().__init__(**kwargs)
        print("B.__init__ end")

    def bbb(self):
        print("bbb super")
        return "bbb"


class C(A, B):
    def __init__(self, **kwargs):
        print("C.__init__ start", kwargs)
        super().__init__(**kwargs)
        print("C.__init__ end")
# 或者
# class C(A, B):
#     def __init__(self, stra, strb, **kwargs):  # ✅ 写出所有父类参数
#         super().__init__(stra=stra, strb=strb, **kwargs)
    # 重写父类方法

    def bbb(self):
        # 访问父类的方法
        print(super().bbb())  # 自动绑定self
        print(super().bbb())
        print(super().bbb())
        return "ccc"


cc = C(stra="a", strb="b")

print(cc.stra, cc.strb, cc.strc, B.bbb(cc), cc.bbb())  # a b 1 bbb ccc、


# 训练
class Person():
    def __init__(self, age, sex, **kwargs) -> None:
        self.age = age
        self.sex = sex
        super().__init__(**kwargs)

    def say(self):
        print(f"person {self.age},{self.sex}")


class Student(Person):
    def __init__(self, age, sex, **kwargs) -> None:
        super().__init__(age, sex, **kwargs)

    def say(self):
        print(f"student {self.age},{self.sex}")


stu = Student(29, "male")
per = Person(20, "fmale")
print(f"stu {stu.age},{stu.sex}")
print(f"per {per.age},{per.sex}")
stu.say()
per.say()
