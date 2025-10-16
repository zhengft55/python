# 封装
# 1 将属性/方法 进行私有化
# 属性/方法 以__开头，只能在本类内部使用
class Example:

    __private_var = 1

    def __init__(self, private_var):
        self.__private_var = private_var  # 私有属性

    def set_private_var(self, private_var):
        self.__private_var = private_var

    def get_private_var(self):
        return self.__private_var

    def __private_method(self):  # 私有方法
        print("这是一个私有方法")
        return "私有"

    def public_method(self):
        print("这是一个公共方法，可以在外部调用")
        # 类内部可以访问私有属性和私有方法
        print(self.__private_var)
        self.__private_method()


example = Example(29)
print(example._Example__private_method())
# print(example.__private_var)  # 这行会报错！外部无法直接访问私有属性
# example.__private_method()    # 这行也会报错！外部无法直接访问私有方法

example.public_method()  # 外部可以调用公共方法，间接访问私有成员
example.set_private_var(20)
example.__private_var = 30  # 动态创建
print(example.get_private_var())
print(example.__private_var)
print(Example._Example__private_var)
print(example._Example__private_var)
