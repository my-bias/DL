import random


def adjust(li, low, high):
    """
    小根堆
    :param li:
    :param low: 堆顶
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i 开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置上有数
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # 将指针j 指向右孩子
        if li[j] < tmp:  # 如果指向的孩子比tmp大 就互换位置
            li[j], li[i] = li[i], li[j]
            # 更新指针 向下看一层
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放到某一级领导上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def topk(li, k):
    # 建堆
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        adjust(heap, i, k - 1)
    # 遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            adjust(heap, 0, k - 1)
    # 出数
    for i in range(k - 1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        adjust(heap, 0, i - 1)
    return heap


li = [i for i in range(100)]

random.shuffle(li)
print(li)
print(topk(li, 5))
