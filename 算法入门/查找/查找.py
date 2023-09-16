def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


li = [5, 8, 9, 4, 6, 2]
ind = linear_search(li, 4)
print(ind)


# 二分法查找
def binary_search(li, val):
    lift = 0
    right = len(li) - 1
    while lift <= right:
        mid = (lift + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            lift = mid + 1
    else:
        return None


li = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
print(binary_search(li, 18))
