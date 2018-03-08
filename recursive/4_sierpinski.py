# -*- coding:utf-8 -*-
def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']

    drawTriangel(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2]), degree-1,])