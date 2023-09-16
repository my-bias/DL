"""
初始时手里(有序区)只有一张牌
每次(从无序区)摸一张牌,插入到手里已有牌的正确位置
"""


def insert_sort(li):
    for i in range(1, len(li)):
        j = i
        tmp = li[i]
        while li[j] < li[j - 1] and j > 0:
            li[j] = li[j - 1]
            li[j - 1] = tmp
            j -= 1
    return li


li = [3, 2, 5, 1, 8, 9, 4]
print(insert_sort(li))
