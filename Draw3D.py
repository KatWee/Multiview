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

            #x max plane
            if start[0] == max :
                self.JumpTo(startYZ[0],startYZ[1])
                self.t.pendown()
                #horizon edge
                if start[0] == end[0] and start[1] < end[1] :
                    self.GoRight(startYZ, endYZ)
                #vertical edge
                elif start[0] == end[0] and start[2] < end[2] :
                    self.GoUp(startYZ, endYZ)
                #slanting edge
                elif start[0] > end[0] and start[0] == max:
                    self.GoBackPlane(start[0], end[0])

            #for the other plane
            else :
                self.JumpTo(startYZ[0],startYZ[1])
                self.GoBackPlane(max, start[0])
                self.t.pendown()
                #horizon edge
                if start[0] == end[0] and start[1] < end[1] :
                    self.GoRight(startYZ, endYZ)
                #vertical edge
                elif start[0] == end[0] and start[2] < end[2] :
                    self.GoUp(startYZ, endYZ)
                #slanting edge
                elif start[0] > end[0] :
                    self.GoBackPlane(start[0], end[0])
        turtle.done()


    def FindMaxX(self):
        max = 0
        for vertice in self.verticies:
            if vertice[0] > max:
                max = vertice[0]
        return max


    def JumpTo(self, startY, startZ):
        self.t.penup()
        self.t.goto(startY, startZ)


    def GoRight(self, startYZ, endYZ) :
        goRight = endYZ[0] - startYZ[0]
        self.t.forward(goRight)


    def GoUp(self, startYZ, endYZ) :
        self.t.left(90)
        goUp = endYZ[1] - startYZ[1]
        self.t.forward(goUp)
        self.t.right(90)


    def GoBackPlane(self, startX, endX):
        self.t.left(30)
        goback = startX*5 - endX*5
        self.t.forward(goback)
        self.t.right(30)