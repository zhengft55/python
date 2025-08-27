# 数据类型隐式转换
# 当不同数据类型一起运算时，Python会自动进行类型转换（隐式转换），通常是向更高精度的类型转换

a = 10      # int类型
b = 2.5     # float类型
c = a + b   # int和float相加，int会自动转换为float
print(f"隐式转换示例：{a}（类型：{type(a)}） + {b}（类型：{type(b)}） = {c}（类型：{type(c)}）")
# 输出：隐式转换示例：10（类型：<class 'int'>） + 2.5（类型：<class 'float'>） = 12.5（类型：<class 'float'>）

# 运算时 类型向高精度转换
# 例如：int + float -> float，int + complex -> complex
d = 3
e = 4 + 5j
f = d + e
print(f"高精度转换示例：{d}（类型：{type(d)}） + {e}（类型：{type(e)}） = {f}（类型：{type(f)}）")
# 输出：高精度转换示例：3（类型：<class 'int'>） + (4+5j)（类型：<class 'complex'>） = (7+5j)（类型：<class 'complex'>）

# 显示转换（强制转换）
# 可以使用int()、float()、str()等函数进行类型强制转换
num_str = "123"
num_int = int(num_str)  # 字符串转整数
print(f"字符串'{num_str}'强制转换为整数：{num_int}（类型：{type(num_int)}）")

num_float = float(num_int)  # 整数转浮点数
print(f"整数{num_int}强制转换为浮点数：{num_float}（类型：{type(num_float)}）")

num_str2 = str(num_float)  # 浮点数转字符串
print(f"浮点数{num_float}强制转换为字符串：'{num_str2}'（类型：{type(num_str2)}）")

# 显示转换注意事项
# 1. 不是所有字符串都能直接转换为数字，比如"abc"就不能转换为int或float
invalid_str = "abc"
try:
    invalid_int = int(invalid_str)
except ValueError as e:
    print(f"字符串'{invalid_str}'无法转换为整数，错误信息：{e}")

# 2. 浮点字符串转int时，需先转为float再转为int
float_str = "3.14"
try:
    float_num = float(float_str)
    int_num = int(float_num)
    print(f"字符串'{float_str}'先转float再转int：{int_num}")
except ValueError as e:
    print(f"转换失败，错误信息：{e}")
