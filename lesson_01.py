# 常用制表符示例

# \t - 水平制表符（Tab键）
print("姓名\t年龄\t职业")
print("张三\t25\t程序员")
print("李四\t30\t设计师")

# \n - 换行符（新行）
print("第一行\n第二行\n第三行")

# \r - 回车符（光标回到行首，从头替换）
print("原始文本1\r新文本")

# \v - 垂直制表符（较少使用）
print("第一行\v第二行")

# \f - 换页符（较少使用）
print("第一页\f第二页")

# \b - 退格符（删除前一个字符）
print("Hello\b World")  # 输出: Hell World

# 组合使用示例
print("产品名称\t价格\t库存\n苹果\t\t5.00\t100\n香蕉\t\t3.50\t80")

# 原始字符串（避免转义）
print(r"这是原始字符串: \t \n 不会被转义")

# 使用format格式化制表符
data = [("张三", 25, "程序员"), ("李四", 30, "设计师")]
for name, age, job in data:
    print("{}\t{}\t{}".format(name, age, job))
