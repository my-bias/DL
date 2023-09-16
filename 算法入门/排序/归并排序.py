# 归并的思想:将列表分解,直至分成一个元素 因为一个元素是有序的 将两个有序列表归并，直至归并为一个列表
import random


# 先假设两边有序
# 归并函数
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high + 1] = tmp
    return li


def _merge_sort(li, low, high):
    mid = (low + high) // 2
    if low < high:
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


def merge_sort(li):
    _merge_sort(li, 0, len(li) - 1)
    return li


li = [i for i in range(10)]


random.shuffle(li)
merge_sort(li)
print(li)
