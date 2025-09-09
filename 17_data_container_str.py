# python中处理文本数据是使用str对象，也称为字符串对象。 字符串是由Unicode码位构成的不可变序列。
# Unicode码是一种字符串编码，ord()函数可以获取字符的Unicode码位，chr()函数可以获取Unicode码位对应的字符。
print(ord('a'))
print(chr(97))
# 字符串支持索引和切片，索引从0开始，切片从1开始。索引必须在指定范围内
str1 = "Hello, World!"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])

# 字符换的遍历，for和while
for i in str1:
    print(i)

i = 0
while i < len(str1):
    print(str1[i])
    i += 1

# 分隔符也可以用字符串， 单个字符 * 个数
print("*" * 10)

# 索引必须在指定范围内，否则会报错， 默认第一个索引值为0，表示从前往后数，最后一个索引值为-1，表示从后往前数
print(str1[10])
print(str1[-1])
print(str1[-2])

# 字符串是不可变序列，不能修改字符串中的元素
# str1[0] = 'H'

# 字符串长度没有固定的限制，取决于计算机内存大小

# 字符串的常用方法和操作详解
# 1. 使用.count()方法统计元素个数
count = str1.count('l')
print(f"字符l出现的次数：{count}")
# 2. 使用.index()方法查找元素索引（返回第一个匹配元素的索引）
index = str1.index('l')
print(f"字符l的索引：{index}")
# 3. 使用.len()方法统计元素个数
length = len(str1)
print(f"字符串长度：{length}")
# 4. 使用.max()方法查找最大值
max = max(str1)
print(f"字符串最大值：{max}")
# 5. 使用.min()方法查找最小值
min = min(str1)
print(f"字符串最小值：{min}")
# 6. 使用.in和not in判断元素是否存在
print(f"字符l是否存在：{'l' in str1}")
print(f"字符x是否存在：{'x' in str1}")
# 7. 使用.join()方法连接字符串
str2 = ''.join(str1)
print(f"连接后的字符串：{str2}")
# 8. 使用.split()方法分割字符串
str3 = str1.split(' ')
print(f"分割后的字符串：{str3}")
# 9. 使用.replace()方法替换字符串
str4 = str1.replace('l', 'L')
print(f"替换后的字符串：{str4}")
# 10. 使用.strip()方法去除字符串两端的空格
str5 = str1.strip()
print(f"去除空格后的字符串：{str5}")
# 11. 使用.startswith()和.endswith()方法判断字符串是否以指定字符串开头或结尾
print(f"字符串是否以H开头：{str1.startswith('H')}")
print(f"字符串是否以!结尾：{str1.endswith('!')}")
# 12. 使用.format()方法格式化字符串
str6 = "我的名字是{}，我的年龄是{}，我的职业是{}".format("张三", 25, "程序员")
print(f"格式化后的字符串：{str6}")
# 13. 使用.upper()和.lower()方法将字符串转换为大写或小写
print(f"大写后的字符串：{str1.upper()}")
print(f"小写后的字符串：{str1.lower()}")
# 14. 使用.splitlines()方法将字符串按行分割
str7 = "Hello\nWorld\nPython"
print(f"按行分割后的字符串：{str7.splitlines()}")
