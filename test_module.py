__all__ = ["test_module"]


def test_module():
    print("test_module")


def test_module2():
    print("test_module2")


# 使用__name__获取模块名，可以避免模块中测试代码的执行
if __name__ == "__main__":
    test_module()
    test_module2()
