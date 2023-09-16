def bucket_sort(li, n=100, max_num=10000):
    # 创建桶
    buckets = [[] for _ in range(n)]
    # 将值放进各自的桶里
    for val in li:
        i = min(val // (max_num // n), n - 1)  # i 表示val放到几号桶中
        buckets[i].append(val)
        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    li.clear()
    # 将桶整合到一起
    for buc in buckets:
        li.extend(buc)
    return li


li = [1, 4, 5, 3, 2, 8, 6, 4, 2, 3, 1, 0]
print(bucket_sort(li))
