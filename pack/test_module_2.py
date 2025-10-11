__all__ = ["test_module_2"]


def test_module_2():
    print("test_module_2")


def test_module2_2():
    print("test_module2_2")


# 使用__name__获取模块名，可以避免模块中测试代码的执行
if __name__ == "__main__":
    test_module_2()
    test_module2_2()
