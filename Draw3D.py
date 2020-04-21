# import pygame
# from pygame.locals import *

# from OpenGL.GL import *
# from OpenGL.GLU import *

# class Draw3D :

#     def __init__(self, edges, verticies):
#         self.edges = edges,
#         self.verticies = verticies


#     def Draw3D(self):
#         glBegin(GL_LINES)
#         glColor3fv((1, 1, 1))

#         for edge in self.edges[0]:
#             for vertex in edge:
#                 glVertex3fv(self.verticies[vertex])
#         glEnd()


#     def show3D(self):
#         pygame.init()
#         display = (800,600)
#         pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

#         gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

#         glTranslatef(0.0,0.0, -40)

#         glRotatef(90, 0, 0, -1)
#         glRotatef(90, 0, -1, 0)
#         glRotatef(30, 0, 0, -1)

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()

#             glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#             self.Draw3D()
#             pygame.display.flip()
#             pygame.time.wait(10)


import turtle
import time
class Draw3D:

    def __init__(self, edges, verticies):
        self.edges = edges
        self.verticies = verticies
        self.t = turtle.Turtle()
        self.s = turtle.Screen()


    def show3D(self):
        self.s.title("3D")
        self.s.screensize(800,800,bg="white")
        self.t.pencolor("black")
        self.t.pensize(3)

        max = self.FindMaxX()

        for edge in self.edges:
            start = self.verticies[edge[0]]
            startYZ = (start[1]*10,start[2]*10)

            end = self.verticies[edge[1]]
            endYZ = (end[1]*10,end[2]*10)

            #for the frontest plane
            if start[0] == end[0] and start[0] == max:
                self.SamePlane(startYZ, endYZ)
            elif start[0] > end[0] and start[0] == max:
                self.GoToBackPlane(startYZ, start[0], end[0])

            #for the other planes
            elif start[0] == end[0] and start[1] < end[1] :
                self.BackPlaneGoRight(max, start[0], startYZ, endYZ)
            elif start[0] == end[0] and start[2] < end[2] :
                self.BackPlaneGoUp(max, start[0], startYZ, endYZ)
            elif start[0] > end[0] :
                self.BackPlaneGoUp(max, start[0], startYZ, endYZ)

        turtle.done()


    def FindMaxX(self):
        max = 0
        for vertice in self.verticies:
            if vertice[0] > max:
                max = vertice[0]
        return max


    def SamePlane(self, startYZ, endYZ):
        self.t.penup()
        self.t.goto(startYZ[0],startYZ[1])
        self.t.pendown()
        self.t.goto(endYZ[0],endYZ[1])
        self.t.penup()


    def GoToBackPlane(self, startYZ, startX, endX):
        self.t.penup()
        self.t.goto(startYZ[0],startYZ[1])
        self.t.pendown()
        self.t.left(30)
        goback = startX*5 - endX*5
        self.t.forward(goback)
        self.t.right(30)
        self.t.penup()


    def BackPlaneGoRight(self, max, startX, startYZ, endYZ):
        self.t.penup()
        self.t.goto(startYZ[0],startYZ[1])
        self.t.left(30)
        goback = max*5 - startX*5
        self.t.forward(goback)
        self.t.right(30)

        goright = endYZ[0] - startYZ[0]
        self.t.pendown()
        self.t.forward(goright)
        self.t.penup()

    def BackPlaneGoUp(self, max, startX, startYZ, endYZ):
        self.t.penup()
        self.t.goto(startYZ[0],startYZ[1])
        self.t.left(30)
        goback = max*5 - startX*5
        self.t.forward(goback)
        self.t.right(30)

        goup = endYZ[1] - startYZ[1]
        self.t.pendown()
        self.t.left(90)
        self.t.forward(goup)
        self.t.right(90)
        self.t.penup()
