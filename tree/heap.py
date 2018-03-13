# -*- coding:utf-8 -*-
# 对的次序性是指父节点的key小许等于子节点的key(最小堆)
# 或父节点的key大于等于子节点的key(最大堆)
# 用列表保存顺序, 父节点索引为p, 左子节点位置为2p, 右子节点位置为2p+1
# 有子节点位置m，查找父节点位置为m//2
# 第一个元素为0

class BinHeap(object):
    def __init__(self):

        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
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


