# 键盘输入
# input()函数用于从键盘获取用户输入
# 所有通过input()获取的数据都是字符串类型

print("=== 1. 基本的键盘输入 ===")
# 最简单的输入方式
name = input("请输入您的姓名：")
print(f"您好，{name}！")

# 输入提示可以为空
age_str = input()  # 没有提示信息
print(f"您输入的内容是：{age_str}")

print("\n=== 2. 输入数据类型转换 ===")
# input()返回的总是字符串，需要手动转换类型

# 转换为整数
age_str = input("请输入您的年龄：")
age = int(age_str)  # 将字符串转换为整数
print(f"您的年龄是：{age}岁，类型是：{type(age)}")

# 转换为浮点数
height_str = input("请输入您的身高（米）：")
height = float(height_str)  # 将字符串转换为浮点数
print(f"您的身高是：{height}米，类型是：{type(height)}")

# 直接在input中转换（常用写法）
weight = float(input("请输入您的体重（公斤）："))
print(f"您的体重是：{weight}公斤")

print("\n=== 3. 多个值的输入 ===")
# 方式1：分别输入
print("请分别输入您的信息：")
student_name = input("姓名：")
student_id = input("学号：")
grade = int(input("年级："))

print(f"学生信息 - 姓名：{student_name}，学号：{student_id}，年级：{grade}")

# 方式2：一行输入多个值（用空格分隔）
print("请输入三个数字，用空格分隔：")
numbers_str = input()
# 使用split()方法分割字符串
number_list = numbers_str.split()  # 默认按空格分割
print(f"输入的字符串列表：{number_list}")

# 转换为整数列表
numbers = [int(x) for x in number_list]
print(f"转换后的整数列表：{numbers}")

# 或者使用map函数一次性转换
print("请再输入三个数字，用空格分隔：")
a, b, c = map(int, input().split())
print(f"a = {a}, b = {b}, c = {c}")

print("\n=== 4. 输入验证和错误处理 ===")
# 处理类型转换错误
while True:
    try:
        user_age = int(input("请输入您的年龄（必须是整数）："))
        print(f"您的年龄是：{user_age}岁")
        break  # 输入正确，跳出循环
    except ValueError:
        print("错误：请输入一个有效的整数！")

# 输入范围验证
while True:
    score = float(input("请输入您的考试成绩（0-100）："))
    if 0 <= score <= 100:
        print(f"您的成绩是：{score}分")
        break
    else:
        print("错误：成绩必须在0-100之间！")

print("\n=== 5. 实际应用示例 ===")
# 示例1：简单计算器
print("=== 简单计算器 ===")
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符（+、-、*、/）：")
num2 = float(input("请输入第二个数字："))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("错误：除数不能为零！")
        result = None
else:
    print("错误：不支持的运算符！")
    result = None

if result is not None:
    print(f"计算结果：{num1} {operator} {num2} = {result}")

# 示例2：学生信息收集
print("\n=== 学生信息收集系统 ===")
student_info = {}
student_info['姓名'] = input("请输入学生姓名：")
student_info['性别'] = input("请输入性别（男/女）：")
student_info['年龄'] = int(input("请输入年龄："))
student_info['专业'] = input("请输入专业：")

# 输入多门课程成绩
print("请输入三门课程的成绩：")
subjects = ['语文', '数学', '英语']
scores = []
for subject in subjects:
    score = float(input(f"{subject}成绩："))
    scores.append(score)

student_info['成绩'] = scores
student_info['平均分'] = sum(scores) / len(scores)

print("\n=== 学生信息汇总 ===")
print(f"姓名：{student_info['姓名']}")
print(f"性别：{student_info['性别']}")
print(f"年龄：{student_info['年龄']}岁")
print(f"专业：{student_info['专业']}")
print(f"各科成绩：")
for i, subject in enumerate(subjects):
    print(f"  {subject}：{scores[i]}分")
print(f"平均分：{student_info['平均分']:.2f}分")

print("\n=== 6. 输入的特殊情况处理 ===")
# 处理空输入
user_input = input("请输入内容（可以为空）：")
if user_input.strip():  # strip()去除首尾空格，然后检查是否为空
    print(f"您输入了：{user_input}")
else:
    print("您没有输入任何内容")

# 处理包含空格的输入
full_name = input("请输入您的全名（可包含空格）：")
print(f"您的全名是：'{full_name}'")

# 大小写处理
answer = input("您喜欢编程吗？(是/否)：").lower()  # 转换为小写
if answer in ['是', '对', 'yes', 'y']:
    print("太好了！编程很有趣！")
elif answer in ['否', '不', 'no', 'n']:
    print("没关系，每个人都有自己的兴趣。")
else:
    print("请回答'是'或'否'。")

print("\n=== 7. 输入格式化示例 ===")
# CSV格式输入（逗号分隔）
print("请输入学生信息，格式：姓名,年龄,成绩")
csv_input = input()
name, age, score = csv_input.split(',')
# 去除可能的空格并转换类型
name = name.strip()
age = int(age.strip())
score = float(score.strip())
print(f"解析结果 - 姓名：{name}，年龄：{age}，成绩：{score}")

# 键值对输入
print("请输入配置信息，格式：键=值")
config_input = input()
key, value = config_input.split('=')
print(f"配置项：{key.strip()} = {value.strip()}")

print("\n=== 8. 输入提示优化 ===")
# 提供默认值的输入
default_city = "北京"
city = input(f"请输入您所在的城市（默认：{default_city}）：") or default_city
print(f"您所在的城市是：{city}")

# 多选输入
print("请选择您的兴趣爱好（可多选，用逗号分隔）：")
print("1. 读书  2. 运动  3. 音乐  4. 旅游  5. 编程")
hobbies_input = input("请输入选项编号：")
hobby_numbers = [int(x.strip()) for x in hobbies_input.split(',')]
hobby_names = {1: '读书', 2: '运动', 3: '音乐', 4: '旅游', 5: '编程'}
selected_hobbies = [hobby_names[num]
                    for num in hobby_numbers if num in hobby_names]
print(f"您的兴趣爱好：{', '.join(selected_hobbies)}")

print("\n=== 输入函数使用总结 ===")
print("1. input()总是返回字符串类型")
print("2. 需要其他类型时要手动转换：int(), float(), bool()")
print("3. 使用split()可以分割输入的字符串")
print("4. 使用map()和split()可以批量转换类型")
print("5. 使用try-except处理输入错误")
print("6. 使用strip()去除首尾空格")
print("7. 提供清晰的输入提示可以改善用户体验")
