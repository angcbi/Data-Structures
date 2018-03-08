# -*- coding:utf-8 -*-
"""
汉诺塔问题，理解为递归问题
假设A, B, C 分别为原始柱子，中间柱子， 目的柱子
1. 先把上面n-1个圆盘移动到A移动到B
2. 把A上最后一个圆盘从A移动到C
3. 把B上n-1个圆盘从B, 移动到C
4, 第三部又可重复1-3步， 停止条件是A上的圆盘数量为0，
5. 共移动次数为2^n -1
"""

def moveDisk(fp, tp):
    print 'move', fp[-1], 'from', fp, 'to', tp
    tp.append(fp.pop())
    print from_pole, with_pole, to_pole

def movePole(length, fromPole, toPole, withPole):
    if length >= 1:
        movePole(length-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        movePole(length-1, withPole, toPole, fromPole)


if __name__ == '__main__':
    from_pole, with_pole, to_pole = [5, 4, 3, 2, 1], [], []
    length = len(from_pole)
    movePole(length, from_pole, to_pole, with_pole)
