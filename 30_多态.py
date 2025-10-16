# 多态（Polymorphism）说明与例子

# 多态指的是：不同类的对象可以通过同一个接口（同一方法名）实现不同的功能。
# 也就是说，调用同一个方法时，不同的对象会表现出不同的行为，
# 这样可以让代码更加灵活、通用。

# 1. 基本说明：
# 在继承体系中，父类定义一个方法，子类重写（override）这个方法。
# 使用父类变量（或形参）引用子类对象，并调用方法时，会自动调用子类的实现（动态绑定）。

# 2. 例子：

class Animal:
    def speak(self):
        print("动物发出叫声")


class Dog(Animal):
    def speak(self):
        print("小狗汪汪叫")


class Cat(Animal):
    def speak(self):
        print("小猫喵喵叫")

# 统一接口


def animal_speak(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
animal = Animal()

animal_speak(dog)    # 输出：小狗汪汪叫
animal_speak(cat)    # 输出：小猫喵喵叫
animal_speak(animal)  # 输出：动物发出叫声

# 这样，无需关心animal具体是哪种动物对象，都可以执行对应的speak方法，实现多态性。

# 通常多态作用于继承体系，但实际上，只要不同对象具有相同的方法（比如speak），就可以实现“鸭子类型”多态。
# 例如，即使没有继承Animal类，只要有speak方法，也能被animal_speak函数使用：


class Duck:
    def speak(self):
        print("鸭子嘎嘎叫")


my_duck = Duck()
animal_speak(my_duck)   # 输出：鸭子嘎嘎叫

# 这里并没有继承Animal类，但由于有speak方法，也可以和前面的Dog、Cat一样被animal_speak调用。
# 这就是“只要像鸭子一样走路和叫，就可以当作鸭子”——即“鸭子类型”。


# isinstance函数用于判断一个对象是否是某个类（或其子类）的实例。
# 语法：isinstance(obj, classinfo)
#   - obj：要判断的对象
#   - classinfo：可以是一个类型或类型元组

# 例子：
print(isinstance(dog, Dog))        # True，因为dog是Dog的实例
print(isinstance(dog, Animal))     # True，因为Dog继承自Animal
print(isinstance(cat, Dog))        # False，cat不是Dog的实例
print(isinstance(my_duck, Animal))  # False，Duck没有继承Animal

# isinstance也可以判断多个类型：
print(isinstance(cat, (Dog, Cat)))  # True，因为cat是Cat的实例


# 当调用对象成员的时候，会和对象本身动态绑定，而不是一直追溯到父类
# 例子：
class Base:
    kind = "父类"

    def show(self):
        # 访问 self.kind 时，Python 的查找顺序是：实例属性 → 类属性 → 父类属性
        """
        Base.show(self)
        │
        └─→ self.kind
             │
             └─→ 实例 obj2 没有 → 去类 Sub 查 → 找到 kind = "子类"

        """
        print(f"{self.kind} 的 show 方法")


class Sub(Base):
    kind = "子类"

    # def show(self):
    #     print(f"{self.kind} 的 show 方法")


# obj1 = Base()
obj2 = Sub()

# obj1.show()  # 输出: 父类 的 show 方法
obj2.show()  # 输出: 子类 的 show 方法

# 动态绑定也适用于类属性:
# print(obj1.kind)  # 输出: 父类
print(obj2.kind)  # 输出: 子类

# 即使变量类型是Base，只要实际对象是Sub，调用的就是Sub中重写的方法，实现动态绑定（多态）。


# practice
class Employee:
    def __init__(self, name, salary, bonus=0) -> None:
        self._name = name
        self._salary = salary
        self._bonus = bonus

    def get_annual(self):
        pass


class Worker(Employee):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def get_annual(self):
        return self._salary * 12

    def work(self):
        print("work function")


class Manager(Employee):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def get_annual(self):
        return self._salary * 12 + self._bonus

    def manage(self):
        print("manage function")


def show_emp_annual(emp: Employee):
    return emp.get_annual()


def work(emp: Employee):
    if isinstance(emp, Worker):
        emp.work()
    else:
        emp.manage()


worker1 = Worker(name="jack", salary=100)
manag = Manager(name="tom", salary=100, bonus=9)
print(show_emp_annual(worker1))
print(show_emp_annual(manag))
work(worker1)
work(manag)
