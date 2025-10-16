# 魔术方法（Magic Methods）
#
# 魔术方法是Python类中特殊的方法，通常以双下划线__开头和结尾，例如 __init__、__str__、__len__ 等。
# 这些方法在特定情况下会被Python解释器自动调用，用于实现对象的初始化、字符串表示、运算符重载等功能。
#
# 常见的魔术方法有：
#  - __init__(self, ...): 构造方法，在创建对象时自动调用（用于初始化对象）
#  - __str__(self): 当使用print()输出对象时自动调用（返回字符串表示）
#  - __repr__(self): 用于交互式解释器显示对象信息
#  - __len__(self): 配合len()函数使用
#  - __getitem__(self, key): 支持按下标/键访问
#  - __setitem__(self, key, value): 支持按下标/键赋值
#  - __delitem__(self, key): 支持按下标/键删除
#  - __eq__, __ne__, __lt__, __le__, __gt__, __ge__: 比较运算相关
#  - __add__, __sub__, __mul__, __truediv__ 等：运算符重载相关
#
# ==== 示例1：基本用法 ====

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person对象: {self.name}, 年龄: {self.age}"

    def __len__(self):
        # 这里的定义只是演示，可以根据实际需要自定义逻辑
        return self.age


p = Person("张三", 18)
print(p)            # 自动调用 __str__，输出: Person对象: 张三, 年龄: 18
print(len(p))       # 自动调用 __len__，输出: 18

# ==== 示例2：自定义容器 ====


class MyList:
    def __init__(self, lst):
        self.data = lst

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f"MyList: {self.data}"


ml = MyList([1, 2, 3])
print(len(ml))         # 3
print(ml[1])           # 2
ml[1] = 20
print(ml)              # MyList: [1, 20, 3]
del ml[0]
print(ml)              # MyList: [20, 3]
