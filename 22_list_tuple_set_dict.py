# 冒泡排序算法详解与实现

# 方法1：您的原始实现（已修正）
print("=== 方法1：while循环实现的冒泡排序 ===")
list1 = [24, 69, 70, 57, 13]
print(f"排序前: {list1}".center(50, "-"))

i = 0
j = len(list1)
# 外层循环：控制排序的轮数，每轮确定一个最大值的位置
while j > 1:  # 修正：当j=1时不需要比较，因为只剩一个元素
    # 内层循环：在未排序部分进行相邻元素比较
    while i <= j - 2:  # i <= j-2 确保 i+1 不会越界
        # 如果前一个元素大于等于后一个元素，则交换位置（升序排列）
        if list1[i] >= list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
        i += 1
    j -= 1  # 每轮结束后，减少比较范围（最大值已经"冒泡"到正确位置）
    i = 0   # 重置内层循环的起始位置

print(f"排序后: {list1}")

# 方法2：标准for循环实现（更常见的写法）
print("\n=== 方法2：for循环实现的冒泡排序 ===")
list2 = [24, 69, 70, 57, 13]
print(f"排序前: {list2}")

n = len(list2)
# 外层循环：需要进行n-1轮比较
for i in range(n-1):
    # 内层循环：每轮比较相邻元素，范围逐渐缩小
    for j in range(n-1-i):
        if list2[j] > list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]

print(f"排序后: {list2}")

# 方法3：优化版冒泡排序（提前结束优化）
print("\n=== 方法3：优化版冒泡排序（提前结束） ===")
list3 = [24, 69, 70, 57, 13]
print(f"排序前: {list3}")

n = len(list3)
for i in range(n-1):
    swapped = False  # 标记本轮是否发生交换
    for j in range(n-1-i):
        if list3[j] > list3[j+1]:
            list3[j], list3[j+1] = list3[j+1], list3[j]
            swapped = True

    # 如果本轮没有发生交换，说明数组已经有序，提前结束
    if not swapped:
        print(f"第{i+1}轮后数组已有序，提前结束排序")
        break

print(f"排序后: {list3}")

# 测试已经有序的数组（展示优化效果）
print("\n=== 测试已有序数组的优化效果 ===")
sorted_list = [1, 2, 3, 4, 5]
print(f"已有序数组: {sorted_list}")

n = len(sorted_list)
for i in range(n-1):
    swapped = False
    for j in range(n-1-i):
        if sorted_list[j] > sorted_list[j+1]:
            sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
            swapped = True

    if not swapped:
        print(f"第{i+1}轮后检测到数组已有序，提前结束")
        break

print(f"结果: {sorted_list}")

print("\n=== 冒泡排序算法总结 ===")
print("时间复杂度：")
print("- 最坏情况：O(n²) - 逆序数组")
print("- 最好情况：O(n) - 已有序数组（优化版）")
print("- 平均情况：O(n²)")
print("空间复杂度：O(1) - 原地排序")
print("稳定性：稳定排序（相等元素相对位置不变）")
