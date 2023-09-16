import random


def partition(li, left, right):  # 位置函数 返回分割位置
    tmp = li[left]  # 取出左边第一个数
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] < tmp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [random.randint(0, 1000) for i in range(1000)]
quick_sort(li, 0, len(li) - 1)
print(li)
