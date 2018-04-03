# -*- coding:utf-8 -*-
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]


    for bucket in d:
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)


"""
bfs(Breadth-first search)广度优先搜索， 是一种图搜索算法从根节点开始，沿着树的宽度遍历树的节点，如果所有节点都访问到，算法终止
实现方法:
a.选取一个节点作为根节点，加入队列(队列保证了搜索顺序，按照层进行)， 并将其染色为灰色, 其余为白色
b.从队列中取出一个节点，搜索其所有子节点，并加入队列, 已访问过节点为黑色，未访问过节点为白色，灰色表示已经被发现并加入队列
c.重复a, b 步骤，直到度列为空
d.标色为了防止重复访问，黑色表示节点已被搜索过子节点， 白色表示该节点尚未被搜索子节点，灰色表示节点已在队列中
"""
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.eenqueue(nbr)

        currentVert.setColor('black')
