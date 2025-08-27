# 字符串驻留机制（String Interning）详细用例

# 字符串驻留机制是Python的一种内存优化技术
# 当创建相同内容的字符串时，Python会重用已存在的字符串对象
# 这样可以节省内存并提高字符串比较的效率

import sys
print("=== 1. 基本字符串驻留示例 ===")
# 小字符串会自动被驻留
a = "hello"
b = "hello"
print(f"a的id: {id(a)}")
print(f"b的id: {id(b)}")
print(f"a is b: {a is b}")  # True，说明是同一个对象

print("\n=== 2. 数字字符串驻留 ===")
# 纯数字字符串通常会被驻留
num1 = "123"
num2 = "123"
print(f"num1 is num2: {num1 is num2}")  # True

print("\n=== 3. 长字符串不自动驻留 ===")
# 较长的字符串可能不会自动驻留
long1 = "这是一个很长的字符串，包含了很多内容，可能不会被自动驻留"
long2 = "这是一个很长的字符串，包含了很多内容，可能不会被自动驻留"
print(f"long1 is long2: {long1 is long2}")  # 可能是False

print("\n=== 4. 包含特殊字符的字符串 ===")
# 包含空格或特殊字符的字符串可能不会被驻留
space1 = "hello world"
space2 = "hello world"
print(f"space1 is space2: {space1 is space2}")  # 可能是False

print("\n=== 5. 使用sys.intern()强制驻留 ===")
# 可以使用sys.intern()强制将字符串驻留
str1 = sys.intern("hello world with spaces")
str2 = sys.intern("hello world with spaces")
print(f"强制驻留后 str1 is str2: {str1 is str2}")  # True

print("\n=== 6. 运行时创建的字符串 ===")
# 运行时动态创建的字符串通常不会被驻留
runtime1 = "".join(["h", "e", "l", "l", "o"])
runtime2 = "".join(["h", "e", "l", "l", "o"])
print(f"runtime1: {runtime1}")
print(f"runtime2: {runtime2}")
print(f"runtime1 is runtime2: {runtime1 is runtime2}")  # False
print(f"runtime1 == runtime2: {runtime1 == runtime2}")  # True

print("\n=== 7. 常量字符串驻留 ===")
# 在代码中直接定义的常量字符串通常会被驻留
const1 = "python"
const2 = "python"
print(f"const1 is const2: {const1 is const2}")  # True

print("\n=== 8. 空字符串和单字符驻留 ===")
# 空字符串和ASCII单字符通常会被驻留
empty1 = ""
empty2 = ""
char1 = "a"
char2 = "a"
print(f"空字符串驻留: {empty1 is empty2}")  # True
print(f"单字符驻留: {char1 is char2}")  # True

print("\n=== 9. 字符串拼接的驻留情况 ===")
# 编译时能确定的字符串拼接会被驻留
compile_time1 = "hello" + "world"
compile_time2 = "hello" + "world"
print(f"编译时拼接驻留: {compile_time1 is compile_time2}")  # True

# 运行时拼接通常不会被驻留
base = "hello"
runtime_concat1 = base + "world"
runtime_concat2 = base + "world"
print(f"运行时拼接驻留: {runtime_concat1 is runtime_concat2}")  # False

print("\n=== 10. 实际应用建议 ===")
# 在实际编程中的建议：
# 1. 不要依赖字符串驻留进行逻辑判断，应该使用 == 而不是 is
# 2. 字符串驻留主要是Python的内部优化，了解即可
# 3. 如果需要频繁比较大量相同的字符串，可以考虑使用sys.intern()

test_str1 = "test"
test_str2 = "test"
print("正确的字符串比较方式:")
print(f"使用 ==: {test_str1 == test_str2}")  # 推荐
print(f"使用 is: {test_str1 is test_str2}")  # 不推荐用于逻辑判断
