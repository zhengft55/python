# 顺序查找
# 顺序查找是一种简单的查找算法，适用于无序列表
# 顺序查找的思路：从列表的第一个元素开始，逐个比较，直到找到目标元素或遍历完整个列表
# 顺序查找的实现：

def seq_search(lst, target):  # pylint: disable=missing-function-docstring
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# list.index() 使用系统函数


def seq_search_optimized(lst, target):  # pylint: disable=missing-function-docstring
    return lst.index(target)

# 列表中有多个要查找的元素，将满足的都返回


def seq_search_multiple(lst, target):  # pylint: disable=missing-function-docstring
    result = []
    for i in range(len(lst)):
        if lst[i] == target:
            result.append(i)
    return result

# 二分查找
# 二分查找是一种高效的查找算法，适用于有序列表
# 二分查找的思路：从列表的中间元素开始，如果中间元素等于目标元素，则返回中间元素的索引，如果中间元素大于目标元素，则继续在中间元素的左边查找，如果中间元素小于目标元素，则继续在中间元素的右边查找
# 二分查找的实现：


def binary_search(lst, target):  # pylint: disable=missing-function-docstring
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        # 这里之所以要对mid加一或减一，是为了缩小查找的范围，避免死循环
        # 如果中间元素lst[mid]大于目标值target，说明目标值只可能在左半部分，所以将右边界right缩小到mid-1
        elif lst[mid] > target:
            right = mid - 1
        # 如果中间元素lst[mid]小于目标值target，说明目标值只可能在右半部分，所以将左边界left扩大到mid+1
        else:
            left = mid + 1
    return -1

# ==========================
# 以下为各方法的运行示例
# ==========================


if __name__ == "__main__":
    # 示例列表
    lst = [5, 3, 7, 3, 9, 1, 3]
    target = 3

    print("原始列表:", lst)
    print("查找目标:", target)

    # 顺序查找
    idx = seq_search(lst, target)
    print("顺序查找结果（返回第一个匹配的索引）:", idx)

    # 使用系统自带的index方法
    try:
        idx_opt = seq_search_optimized(lst, target)
        print("系统index查找结果:", idx_opt)
    except ValueError:
        print("系统index查找结果: 未找到目标元素")

    # 查找所有匹配的索引
    idxs = seq_search_multiple(lst, target)
    print("查找所有匹配的索引:", idxs)

    # 二分查找（需要有序列表）
    sorted_lst = sorted(lst)
    print("有序列表:", sorted_lst)
    idx_bin = binary_search(sorted_lst, target)
    print("二分查找结果（有序列表中第一个匹配的索引）:", idx_bin)

    # 查找不存在的元素
    not_exist = 100
    print("\n查找不存在的元素:", not_exist)
    print("顺序查找结果:", seq_search(lst, not_exist))
    try:
        print("系统index查找结果:", seq_search_optimized(lst, not_exist))
    except ValueError:
        print("系统index查找结果: 未找到目标元素")
    print("查找所有匹配的索引:", seq_search_multiple(lst, not_exist))
    print("二分查找结果:", binary_search(sorted_lst, not_exist))
