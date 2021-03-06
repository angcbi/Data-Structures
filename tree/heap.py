# -*- coding:utf-8 -*-
# 最小堆是指父节点的key小于等于子节点(左子节点和右子节点)的key(最小堆), 最大堆相反
# 以左右孩子为跟的子树也是一个堆
# 或父节点的key大于等于子节点的key(最大堆)
# 用列表保存顺序, 父节点索引为p, 左子节点位置为2p, 右子节点位置为2p+1
# 有子节点位置m，查找父节点位置为m//2
# 第一个元素为0
# python第三方数据结构库pythonds
# from pythonds.trees.binheap import BinHeap


class BinHeap(object):
    def __init__(self):

        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        # 第一个位置添加0是为了方便遍历跟的父节点
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]

            i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)

            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

            i = mc


    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist
        while i > 0:
            self.percDown(i)
            i = i - 1



if __name__ == '__main__':
    bp = BinHeap()
    bp.insert(3)
    bp.insert(10)
    bp.insert(11)
    print bp.heapList
    bp.insert(2)
    print bp.heapList
    bp.insert(0)
    print bp.heapList
    bp.delMin()
    print bp.heapList

    bp.buildHeap([5, 3, 8, 1, 9, 7, 6])
    print bp.currentSize
    print bp.heapList

