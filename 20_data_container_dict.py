# 字典
# 字典是可变序列，字典中的元素是无序的，不重复的，字典中的元素是唯一的，字典中的元素是不可变的。
# 字典中的元素是键值对，键是唯一的，值是可变的。
# 字典的定义 语法：
# 字典名 = {键1: 值1, 键2: 值2, 键3: 值3, ...}
# 例子：
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(f"字典：{dict1}")
print(f"字典类型：{type(dict1)}")

# 创建空字典 语法：dict()，或者dict1 = {}
dict2 = dict()
print(f"空字典：{dict2}, 类型：{type(dict2)}")
dict3 = {}
print(f"空字典：{dict3}, 类型：{type(dict3)}")

# 通过key获取value 语法：字典名[key]
print(dict1['name'])

# 字典的key通常是字符串或数字，若是其他类型，则key必须是不可变类型（元素不可变），value可以是任意数据类型
dict3 = {1: '一', '2': '二', (3, 4): '三'}
print(f"字典：{dict3}")
print(f"字典类型：{type(dict3)}")

# 字典的遍历，for，不支持索引，无while循环
for key in dict1:
    print(key)
for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(key, value)


# 字典的key必须是唯一的，如果定义了多个相同的key，则后面的key会覆盖前面的key
dict4 = {'name': '张三', 'name': '李四'}
print(f"字典：{dict4}")

# 字典的常用方法和操作详解
# 1. 使用.get()方法获取value
print(dict1.get('name'))
# 2. 使用.setdefault()方法设置value
dict1.setdefault('name', '王五')
# 这里打印出来的name是张三，是因为dict1在最开始定义时，'name'对应的值就是'张三'，
# 后面虽然调用了setdefault('name', '王五')，但setdefault方法只有在key不存在时才会设置新值，
# 如果key已经存在，则不会修改原有的值。因此，dict1['name']依然是'张三'。
print(f"字典：{dict1}")
# 3. 使用.pop()方法删除元素，如果key存在于字典中，则删除该键值对，并返回value，如果key不存在于字典中，则返回默认值，默认值为None
print(f"删除的value：{dict1.pop('name')}")
print(f"删除的value：{dict1.pop('name', '未知')}")
print(f"字典：{dict1}")
# 4. 使用.popitem()方法删除元素
dict1.popitem()
print(f"字典：{dict1}")
# 5. 使用.clear()方法清空字典
dict1.clear()
print(f"字典：{dict1}")
# 6. 使用.copy()方法复制字典
dict5 = dict1.copy()
print(f"字典：{dict5}")
# 7. 使用.items()方法获取字典的键值对
print(dict1.items())
# 8. 使用.keys()方法获取字典的键
print(dict1.keys())
# 9. 使用.values()方法获取字典的值
print(dict1.values())
# 10. 使用.update()方法更新字典
dict1.update({'name': '王五'})
print(f"字典：{dict1}")
# 11. 使用.fromkeys()方法创建字典
dict6 = dict.fromkeys(['name', 'age', 'gender'], '未知')
print(f"字典：{dict6}")
# 12. 使用.len()方法统计字典元素个数
print(len(dict1))
# 13. 使用.max()方法查找字典最大值
print(max(dict1))
# 14. 使用.min()方法查找字典最小值
print(min(dict1))
# 15. 使用.in和not in判断元素是否存在
print('name' in dict1)

# del 语句删除字典中的元素、
print(f"字典：{dict1}")
del dict1['name']
print(f"字典：{dict1}")


# 字典生成式
# 语法：
# 字典名 = {表达式 for 变量 in 可迭代对象}
# 例子：
dict7 = {i: i**2 for i in range(1, 11)}
print(f"字典生成式：{dict7}")

# 内置函数zip()详解
# zip() 是 Python 的一个内置函数，可以将多个可迭代对象（如列表、元组等）“打包”成一个迭代器。
# 注意：zip() 返回的不是列表，而是一个迭代器对象（类型为 <class 'zip'>）。
# 这个迭代器每次迭代会返回一个元组，元组中包含每个可迭代对象相同位置的元素。
# 如果需要得到列表，可以使用 list() 函数将 zip() 的结果转换为列表，例如：list(zip(list1, list2))
# 语法：
# zip(可迭代对象1, 可迭代对象2, ...)
# 注意：如果各个可迭代对象长度不一致，则以最短的为准进行“打包”。
# 常见用法举例：

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [True, False, True]

# 将两个列表打包
zipped = zip(list1, list2)
print(f"zip打包两个列表：{list(zipped)}")  # [('a', 1), ('b', 2), ('c', 3)]

# 打包三个列表
zipped3 = zip(list1, list2, list3)
# [('a', 1, True), ('b', 2, False), ('c', 3, True)]
print(f"zip打包三个列表：{list(zipped3)}")

# 如果长度不一致
list4 = [100, 200]
zipped4 = zip(list1, list4)
print(f"zip长度不一致：{list(zipped4)}")  # [('a', 100), ('b', 200)]

# zip对象是一个迭代器，只能遍历一次
z = zip(list1, list2)
print(list(z))  # 第一次遍历有结果
print(list(z))  # 第二次遍历为空列表

# zip常用于字典的快速创建
keys = ['name', 'age', 'gender']
values = ['张三', 18, '男']
dict8 = dict(zip(keys, values))
print(f"使用zip快速创建字典：{dict8}")

# zip也常用于遍历多个序列
for k, v in zip(keys, values):
    print(f"{k}: {v}")
