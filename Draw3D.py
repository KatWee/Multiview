import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Draw3D :

    def __init__(self, edges, verticies):
        self.edges = edges,
        self.verticies = verticies


    def Draw3D(self):
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))

        for edge in self.edges[0]:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()


    def show3D(self):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -40)

        glRotatef(90, 0, 0, -1)
        glRotatef(90, 0, -1, 0)
        glRotatef(30, 0, 0, -1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            self.Draw3D()
            pygame.display.flip()
            pygame.time.wait(10)