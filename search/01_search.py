# -*- coding:utf-8 -*-
def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, pos


def orderedSequentialSearch(alias, item):
    """
    使用while 循环，可以在while 条件中添加break提交
    使用for循环，需要单独添加break条件
    但是不要忘记更改条件(自增或自减)
    """
    pos, found, stop = 0, False, False
    # for value in alias:
    #     if found or stop:
    #         break
    #
    #     if value == item:
    #         found = True
    #     elif value > item:
    #         stop = True
    while pos < len(alias) and not found and not stop:
        if alias[pos] == item:
            found = True
        elif alias[pos] > item:
            stop = True
        else:
            pos = pos + 1

    return found

def binarySearch(alist, item):
    """
    时间复杂度是O(logn)
    """
    first = 0
    last = len(alist) - 1
    found = False
    count = 0

    while first <= last and not found:
        print 'searching start ', first, 'last ', last
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1

        count = count + 1

    return found

def binarySearch_1(alist, item):
    """
    二分搜索，递归版本
    """
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch_1(alist[:midpoint-1], item)
            else:
                return binarySearch_1(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print binarySearch_1(testlist, 100)
print binarySearch_1(testlist, 13)



# testlist = [1, 2, 32, 8, 17, 19]
# print sequentialSearch(testlist, 1)
# print sequentialSearch(testlist, 100)

# l = range(10)
# print orderedSequentialSearch(l, 10)
# print orderedSequentialSearch(l, 3)
