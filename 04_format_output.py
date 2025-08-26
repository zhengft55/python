# 1. %操作符
# 2. format()函数
# 3. f-string


# 定义四个变量，分别为姓名、年龄、职业和城市
name = "张三"
age = 28
job = "前端开发工程师"
city = "上海"

# 1. %操作符  类型一一对应
print("个人信息：%s %.2f %s %s" % (name, age, job, city))
print("个人信息：%s %.2f %s %s", name, age, job, city)

# 2. format()函数 {}内可以不写数字，默认按顺序填充，写数字的话，按index数字顺序填充
print("个人信息：{} {} {} {}".format(name, age, job, city))
print("个人信息：{0} {1} {2} {3}".format(name, age, job, city))

# 3. f-string 推荐使用
print(f"个人信息：{name} {age} {job} {city}")
