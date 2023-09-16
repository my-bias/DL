# 首先知道数的范围


def count_sort(li, maxcount):
    # 创建计数列表
    count = [0 for _ in range(maxcount + 1)]
    # 将值对应的索引计数
    for val in li:
        count[val] += 1
    li.clear()
    print(count)
    # 取出计数值
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


li = [2, 1, 3, 5, 6, 7, 4, 9]
count_sort(li, 10)
print(li)
