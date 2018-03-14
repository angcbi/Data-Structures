# -*- coding:utf-8 -*-
import random

from util import log

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
    最好情况，数据已经排好序， O(n^2)
    """
    for i in range(1, len(alist)):
        temp_index = i
        temp = alist[i]
        # for j in range(i):
        #     # 从后往前比较
        #     if alist[i-j-1] > temp:
        #         alist[temp_index] = alist[i-j-1]
        #         temp_index = i-j-1
        # 采用while循环，减少内层循环次数
        while temp_index > 0 and alist[temp_index-1] > temp:
            alist[temp_index] = alist[temp_index-1]
            temp_index = temp_index - 1

        # 把i插入到正确位置
        alist[temp_index] = temp

    return alist

@log
def shellSort(alist):
    """
    希尔排序块是因为，一次移动了一大步逆序(如升序排列， 后面数字比前面数字大叫逆序)， 冒泡排序每次只能移动一次逆序
    步长公式  n/2^k  称为希尔增量
    希尔博增量 2^k - 1
    """
    length = len(alist)
    # 迭代过程中步长变小，当步长为1时，即为一次完整的插入排序
    # 有几个步长，就划分几个区间
    gap = length // 2

    while gap > 0:
        # 对每个区间进行插入排序
        for i in range(gap):
            # range的step需要定义为步长，即可取到一个区间的所有数据
            # 插入排序需要从第二个元素开始循环，所以开始位置不能是i,而是i+gap
            for j in range(i+gap, length, gap):
                temp = alist[j]
                position = j

                while position >= gap and alist[position-gap] > temp:
                    alist[position] = alist[position-gap]
                    position = position-gap

                alist[position] = temp

        gap = gap // 2

    return alist

@log
def shellSort2(alist):
    # 步长采用2^k - 1
    length = len(alist)
    # 实际步长需要根据列表总长度动态定义
    steps = [1, 3, 7]
    for step in steps[::-1]:
        for i in range(step):
            for j in range(step+i, length, step):
                temp = alist[j]
                temp_index = j

                while temp_index >= step  and alist[temp_index-step] > temp:
                    alist[temp_index] = alist[temp_index-step]
                    temp_index = temp_index-step

                alist[temp_index] = temp

    return alist


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righhalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righhalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(lefthalf):
            if lefthalf[i] < righhalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righhalf[j]
                j = j + 1

            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            
        while j < len(righhalf):
            alist[k] = righhalf[j]
            j = j + 1
            k = k + 1

    return alist



if __name__ == '__main__':
    test_list = [random.randrange(0, 1000) for i in range(10)]
    # test_list = [305, 456, 833, 758, 348, 370, 416, 333, 356, 19]
    # print test_list
    # 复制一份test_list 传给排序函数,可使用list, [:]或copy方法
    # print bubbleSort(list(test_list))
    # print bubbleSort2(list(test_list))
    # print selectionSort(list(test_list))
    # print insertSort(list(test_list))
    # print shellSort(list(test_list))
    print mergeSort(list(test_list))
