# 1. 求list最大值
class A01:

    def __init__(self) -> None:
        pass

    def max(self, list):
        length = len(list)
        for i in range(length-1):
            for j in range(length-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return list


a01 = A01()
print(a01.max([1.1, 2.9, -1.9, 67.9, 60, -3]))
