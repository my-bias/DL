def radix_sort(li):
    it = 0  # 初始迭代次数
    max_num = max(li)
    while 10 ** it <= max_num:
        # 创建桶
        buckets = [[] for _ in range(10)]
        # 分桶
        for val in li:
            ind = (val // 10 ** it) % 10
            buckets[ind].append(val)
        li.clear()
        # 整合桶
        for buc in buckets:
            li.extend(buc)
        # 循环
        it += 1
    return li


li = [9,2,5,4,8,7,1]
radix_sort(li)
print(li)
