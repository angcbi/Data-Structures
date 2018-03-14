# -*- coding:utf-8 -*-
from util import log

@log
def quickSort(alist):
    return qSort(alist, 0, len(alist)-1)

def qSort(alist, start, end):
    if start >= end:
        return alist

    m, n = start, end
    pivot = alist[m]
    while m < n:
        while alist[n] > pivot and m < n:
            n = n - 1

        while alist[m] < pivot and m < n:
            m = m + 1

        alist[m], alist[n] = alist[n], alist[m]

    qSort(alist, start, m-1)
    qSort(alist, m+1, end)

    return alist


@log
def quickSort2(alist):
    """
    额外占用空间
    """
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return quickSort2([x for x in alist if x < pivot]) + [pivot] + quickSort2([x for x in alist if x > pivot])


if __name__ == '__main__':
    test_list = [7, 5, 8, 10, 2, 4]
    print quickSort(test_list)

