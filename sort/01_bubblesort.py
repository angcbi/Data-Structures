# -*- coding:utf-8 -*-
import time
import random
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = int(time.time()*1000)
        res = func(*args, **kwargs)
        print '%s cost %dms' % (func.__name__, time.time()*1000 - start_time)
        return res
    return wrapper

@log
def bubbleSort(alist):
    """
    1. 第一次排序需要和n-1个数比较，比较后，最大的数队首或者队尾
    2. 第二次排序需要和n-2个数字比较
    3. n-1次排序后，剩余的最后一个数字自然在正确位置

    优化1： 如果是升序排列，每次排序后，后面的对应数都在正确位置，第二层无需遍历, 第二次遍历结束条件-i, 少比较1+2+...+n-2次
    优化2: 内层循环，如果完成后没有发生数据交换，说明已经排好序了。可以直接退出, 这种叫做短路冒泡排序，如果一个列表只需几次就交换就可排好，冒泡排序有优势
    优化3：记录内层循环最后数据交换的位置，该位置之后的数据已经是有序的了
    """
    count = 0
    for i in range(len(alist)-1):
        is_ok = True
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                is_ok = False

            count = count + 1

        if is_ok:
            print 'already order'
            break

    return alist

@log
def bubbleSort2(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

@log
def selectionSort(alist):
    """
    选择排序提高了冒泡排序的性能，每次遍历，只进行一次交换，找到最大项，把最大项放到正确位置
    内层排序前，先假设最大值的下标是开始时的位置，每次更新比较后更新最大值下标，内层循环结束后交换位置
    """
    # for i in range(0, len(alist)-1):
    #     max_index = i
    #     for j in range(i+1, len(alist)):
    #         if alist[j] < alist[max_index]:
    #             max_index = j
    #
    #     alist[i], alist[max_index] = alist[max_index], alist[i]
    for fileslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fileslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fileslot], alist[positionOfMax] = alist[positionOfMax], alist[fileslot]

    return alist

@log
def insertSort(alist):
    """
    插入排序是把元素插入到已经排好序的列表中，列表中插入位置之后的元素后以一位，需要循环n-1次
    需要两个变量，一个保存i的值，另外一个保存待插入的位置
    """
    for i in range(1, len(alist)):
        temp_index = i
        temp = alist[i]
        for j in range(i):
            # 从后往前比较
            if alist[i-j-1] > temp:
                alist[temp_index] = alist[i-j-1]
                temp_index = i-j-1

        # 把i插入到正确位置
        alist[temp_index] = temp

    return alist

if __name__ == '__main__':
    test_list = [random.randrange(0, 1000) for i in range(10)]
    print test_list
    # 复制一份test_list 传给排序函数,可使用list, [:]或copy方法
    print bubbleSort(list(test_list))
    print bubbleSort2(list(test_list))
    print selectionSort(list(test_list))
    print insertSort(list(test_list))
