"""
先遍历一遍找到最小的数 , 和第一个数交换 一直往复操作
算法关键点: 有序区 无序区, 无序区最小值的位置
"""


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

    return li


li = [2, 5, 6, 4, 3, 8, 7, 9]
print(select_sort(li))
