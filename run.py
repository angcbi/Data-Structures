# -*- coding:utf-8 -*-
import random

from sort import (bubbleSort, bubbleSort2, selectionSort, insertSort, shellSort,
                  shellSort2, mergeSort, quickSort, quickSort2)


if __name__ == '__main__':
    test_list = [random.randrange(0, 1000) for i in range(100000)]
    # test_list = [305, 456, 833, 758, 348, 370, 416, 333, 356, 19]
    test_list
    # 复制一份test_list 传给排序函数,可使用list, [:]或copy方法
    # print bubbleSort(list(test_list))
    # print bubbleSort2(list(test_list))
    # print selectionSort(list(test_list))
    # print insertSort(list(test_list))
    # print shellSort(list(test_list))
    mergeSort(list(test_list))
    quickSort(list(test_list))
    quickSort2(list(test_list))
