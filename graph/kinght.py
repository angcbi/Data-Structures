# -*- coding:utf-8 -*-
"""
a. 先将实际需求转化为图
b. 采用DFS(Depth First Search)搜索树
c. BFS是一次简历搜素树的一层，而DFS是尽可能深的搜索树的一枝
"""
from pythonds.graphs import Graph


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = postToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = postToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)

    return ktGraph


def postToNodeId(row, column, board_size):
    """
    二维坐标转为为一维线性数值
    """
    return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
    """
    查找所有可用的下一跳位置
    """
    newMoves = []
    moveOffset= [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffset:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and \
           legalCoord(newY, bdSize):
            newMoves.append((newX, newY))

    return newMoves

def legalCoord(x, bdSize):
    """
    检测行或列是否有效
    """
    if x >=0 and x < bdSize:
        return True

    return False


def knightTour(n ,path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)

            i = i + 1

        if not done:
            path.pop()
            u.setColor('white')
        else:
            done = True

    return done

if __name__ == '__main__':
    g = knightGraph(4)
    for v in g:
        for w in v.getConnections():
            print v.getId(), w.getId(), '\n'
