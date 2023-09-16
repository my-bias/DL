# 冒泡排序
"""
列表每两个相邻的数,如果前面的比后面的大,则交换这两个数。
一趟排序完成后,则无序区减少一个数,有序区增加一个数。
# 关键在于 趟 无序区范围
"""

import random


def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟 最后一趟不需要进行
        exchange = False
        for j in range(len(li) - 1 - i):  # 指针的位置
            if li[j] > li[j + 1]:
                li[j + 1], li[j] = li[j], li[j + 1]
                exchange = True
        if not exchange:
            return li


