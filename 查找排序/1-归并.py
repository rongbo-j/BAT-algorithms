"""
一、介绍
   基本思想：
   将数组array[0,...,n-1]中的元素分成两个子数组：array1[0,...,n/2]
   和array2[n/2+1,...,n-1]。分别对这两个数组单独排序，然后将已排序的
   两个子数组归并成一个含有n个元素的有序数组

二、步骤
    递归实现

三、时间复杂度：O(N*logN)

四、归并排序的两点改进
    * 在数组长度比较短的情况下，不进行递归，而是选择其他排序方案，如插入排序
    * 归并过程中，可以用记录数组下标的方式代替申请新内存空间；从而避免array和
      辅助数组间的频繁数据移动
"""


def merge(left, right):  # 合并两个有序数组
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) >> 1
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    return merge(left, right)


# ------------------- 按第二个改进的修改----------------------------

temp = [0] * 100


def Merge(array, low, mid, high):
    i = low
    j = mid + 1
    size = 0
    while i <= mid and j <= high:
        if array[i] < array[j]:
            temp[size] = array[i]
            i += 1
        else:
            temp[size] = array[j]
            j += 1
        size += 1
    while i <= mid:
        temp[size] = array[i]
        size += 1
        i += 1
    while j <= high:
        temp[size] = array[j]
        size += 1
        j += 1
    for i in range(size):
        array[low + i] = temp[i]


def Merge_sort(array, low, high):
    if low >= high:
        return
    mid = (low + high) >> 1
    Merge_sort(array, low, mid)
    Merge_sort(array, mid + 1, high)
    Merge(array, low, mid, high)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Merge_sort(alist, 0, len(alist) - 1)
    print(alist)
