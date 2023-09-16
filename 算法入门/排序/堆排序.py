"""过程:
1.建立堆
2.得到堆顶元素，为最大元素
3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
4.堆顶元素为第二大元素
5.重复3操作
"""

import random


# 堆向下调整
def adjust(li, low, high):
    """
    大根堆
    :param li:
    :param low: 堆顶
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i 开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置上有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # 将指针j 指向右孩子
        if li[j] > tmp:  # 如果指向的孩子比tmp大 就互换位置
            li[j], li[i] = li[i], li[j]
            # 更新指针 向下看一层
            i = j

            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放到某一级领导上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):  # 遍历每个节点进行堆的向下调整
        adjust(li, i, n - 1)
    # 堆建造完成了 主要思想:农村包围城市
    for i in range(n - 1, -1, -1):
        # i 指向最后一个位置
        li[0], li[i] = li[i], li[0]
        adjust(li, 0, i - 1)


li = [i for i in range(1000)]

random.shuffle(li)
print(li)
heap_sort(li)
print(li)
