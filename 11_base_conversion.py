
# Python进制转换详解
# 进制转换是编程中常见的操作，主要涉及二进制(2)、八进制(8)、十进制(10)、十六进制(16)

print("=== 1. Python内置进制转换函数 ===")

# 1.1 十进制转其他进制
decimal_num = 255
print(f"十进制数: {decimal_num}")
print(f"转二进制: {bin(decimal_num)}")    # 0b11111111
print(f"转八进制: {oct(decimal_num)}")    # 0o377
print(f"转十六进制: {hex(decimal_num)}")   # 0xff

print("\n=== 2. 其他进制转十进制 ===")

# 2.1 使用int()函数，第二个参数指定原数字的进制
binary_str = "11111111"      # 二进制字符串
octal_str = "377"            # 八进制字符串
hex_str = "ff"               # 十六进制字符串

print(f"二进制 '{binary_str}' 转十进制: {int(binary_str, 2)}")
print(f"八进制 '{octal_str}' 转十进制: {int(octal_str, 8)}")
print(f"十六进制 '{hex_str}' 转十进制: {int(hex_str, 16)}")

print("\n=== 3. 进制转换公式说明 ===")

# 3.1 十进制转其他进制公式（除法取余法）
print("十进制转其他进制公式：")
print("- 用目标进制数连续除十进制数，取余数")
print("- 余数从下往上排列就是结果")
print("例如：255转二进制")
print("255 ÷ 2 = 127 余 1")
print("127 ÷ 2 = 63  余 1")
print("63  ÷ 2 = 31  余 1")
print("31  ÷ 2 = 15  余 1")
print("15  ÷ 2 = 7   余 1")
print("7   ÷ 2 = 3   余 1")
print("3   ÷ 2 = 1   余 1")
print("1   ÷ 2 = 0   余 1")
print("从下往上读余数：11111111")

# 3.2 其他进制转十进制公式（位权展开法）
print("\n其他进制转十进制公式：")
print("- 每一位数字 × 该位的权值，然后相加")
print("- 权值 = 进制数^位置(从右边第0位开始)")
print("例如：二进制11111111转十进制")
print("1×2^7 + 1×2^6 + 1×2^5 + 1×2^4 + 1×2^3 + 1×2^2 + 1×2^1 + 1×2^0")
print("= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255")

print("\n=== 4. 手动实现进制转换函数 ===")


def decimal_to_base(decimal_num, base):
    """十进制转任意进制"""
    if decimal_num == 0:
        return "0"

    digits = "0123456789ABCDEF"  # 支持16进制
    result = ""

    while decimal_num > 0:
        remainder = decimal_num % base
        result = digits[remainder] + result
        decimal_num = decimal_num // base

    return result


def base_to_decimal(num_str, base):
    """任意进制转十进制"""
    digits = "0123456789ABCDEF"
    result = 0
    num_str = num_str.upper()  # 转大写处理十六进制

    for i, digit in enumerate(reversed(num_str)):
        digit_value = digits.index(digit)
        result += digit_value * (base ** i)

    return result


# 测试手动实现的函数
print("手动实现的转换函数测试：")
print(f"255转二进制: {decimal_to_base(255, 2)}")
print(f"255转八进制: {decimal_to_base(255, 8)}")
print(f"255转十六进制: {decimal_to_base(255, 16)}")

print(f"二进制11111111转十进制: {base_to_decimal('11111111', 2)}")
print(f"八进制377转十进制: {base_to_decimal('377', 8)}")
print(f"十六进制FF转十进制: {base_to_decimal('FF', 16)}")

print("\n=== 5. 常见进制转换对照表 ===")
print("十进制\t二进制\t\t八进制\t十六进制")
print("-" * 40)
for i in range(16):
    print(f"{i}\t{bin(i)[2:]:>8}\t{oct(i)[2:]:>6}\t{hex(i)[2:].upper():>8}")

print("\n=== 6. 实际应用示例 ===")

# 6.1 RGB颜色值转换
rgb_decimal = (255, 0, 128)  # 红、绿、蓝的十进制值
rgb_hex = tuple(hex(color)[2:].upper().zfill(2) for color in rgb_decimal)
print(f"RGB十进制: {rgb_decimal}")
print(f"RGB十六进制: #{rgb_hex[0]}{rgb_hex[1]}{rgb_hex[2]}")

# 6.2 IP地址转换
ip_parts = [192, 168, 1, 1]
ip_binary = [bin(part)[2:].zfill(8) for part in ip_parts]
print(f"IP地址: {'.'.join(map(str, ip_parts))}")
print(f"二进制: {'.'.join(ip_binary)}")

# 6.3 文件权限（八进制）
permissions = 0o755  # 八进制字面量
print(f"文件权限八进制: {oct(permissions)}")
print(f"文件权限十进制: {permissions}")
print(f"文件权限二进制: {bin(permissions)}")

print("\n=== 7. 进制转换技巧总结 ===")
print("1. 使用Python内置函数：bin(), oct(), hex(), int()")
print("2. 二进制与八进制转换：3位二进制 = 1位八进制")
print("3. 二进制与十六进制转换：4位二进制 = 1位十六进制")
print("4. 记住常用数字的进制对应关系")
print("5. 理解位权概念：每一位的权重是进制的幂次")
