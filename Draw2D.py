import turtle
class Draw2D :

    def __init__(self, edges, verticies):
        self.edges = edges
        self.verticies = verticies
        self.tFront = turtle.Turtle()
        self.tBehind = turtle.Turtle()
        self.s = turtle.Screen()


    def show2D(self):
        self.s.title("2D")
        self.s.screensize(800,800,bg="white")

        self.tFront.pencolor("Black")
        self.tFront.pensize(3)
        self.tFront.speed(0)

        self.tBehind.pencolor("Gray")
        self.tBehind.pensize(3)
        self.tBehind.speed(0)

        maxX, minX = self.FindMinMax(0)
        maxY, minY = self.FindMinMax(1)
        maxZ, minZ = self.FindMinMax(2)

        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]

            #front view
            self.DrawFront(start, end, 0)

            #back view
            self.DrawBack(start, end, 0)

            #right view
            self.DrawRight(start, end, 0)

            #left view
            self.DrawLeft(start, end, 0)

            #top view
            self.DrawTop(start, end, 0)

            #bottom view
            self.DrawBottom(start, end, 0)


        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]

            #front view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawFront(start, end, 1)
            #back view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawBack(start, end, 1)

            #right view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawRight(start, end, 1)

            #left view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawLeft(start, end, 1)

            #top view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawTop(start, end, 1)

            #bottom view
            if self.CheckBehind(minX ,maxX, minY, maxY, minZ, maxZ, start, end) :
                self.DrawBottom(start, end, 1)

        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]
            print(start)
            print(maxX,maxY,minY, maxY, minZ, maxZ)

            #front view
            if self.CheckTopPlane(0,maxX,start) :
                self.DrawFront(start, end, 0)

            #back view
            if self.CheckTopPlane(0,minX,start) :
                self.DrawBack(start, end, 0)

            #right view
            if self.CheckTopPlane(1,maxY,start) :
                self.DrawRight(start, end, 0)

            #left view
            if self.CheckTopPlane(1,minY,start) :
                self.DrawLeft(start, end, 0)

            #top view
            if self.CheckTopPlane(2,maxZ,start) :
                self.DrawTop(start, end, 0)

            #bottom view
            if self.CheckTopPlane(2,minZ,start) :
                self.DrawBottom(start, end, 0)

        self.tFront.hideturtle()
        self.tBehind.hideturtle()
        turtle.done()


    def FindMinMax(self, coor) :
        max = 0
        min = 0
        for vertice in self.verticies:
            if vertice[coor] > max:
                max = vertice[coor]
            if vertice[coor] < min:
                min = vertice[coor]
        return max, min


    def JumpTo(self, coor1, coor2) :
        self.tFront.penup()
        self.tFront.goto(coor1, coor2)
        self.tBehind.penup()
        self.tBehind.goto(coor1, coor2)


    def DrawLine(self, coor1, coor2) :
        self.tFront.pendown()
        self.tFront.goto(coor1, coor2)
        self.tFront.penup()


    def DrawLineBehind(self, coor1, coor2) :
        self.tBehind.pendown()
        self.tBehind.goto(coor1, coor2)
        self.tBehind.penup()

    def CheckBehind(self,minX, maxX, minY, maxY, minZ, maxZ, start, end):
        if ((start[0] > minX and
        start[0] < maxX and
        start[1] > minY and
        start[1] < maxY and
        start[2] > minZ and
        start[2] < maxZ) or
        (end[0] > minX and
        end[0] < maxX and
        end[1] > minY and
        end[1] < maxY and
        end[2] > minZ and
        end[2] < maxZ)) :
            return 1
        else :
            return 0


    def CheckTopPlane(self,coor,top,start) :
        if start[coor] == top:
            return 1
        else :
            return 0


    def DrawFront(self, start, end, behind) :
        startY = start[1] * 5
        startZ = start[2] * 5
        endY = end[1] * 5
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        if behind == 1 :
            self.DrawLineBehind(endY, endZ)
        else :
            self.DrawLine(endY, endZ)


    def DrawBack(self, start, end, behind) :
        startY = -start[1] * 5 - 200
        startZ = start[2] * 5
        endY = -end[1] * 5 - 200
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        if behind == 1 :
            self.DrawLineBehind(endY, endZ)
        else :
            self.DrawLine(endY, endZ)


    def DrawRight(self, start, end, behind) :
        startX = -start[0] * 5 + 100
        startZ = start[2] * 5
        endX = -end[0] * 5 + 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        if behind == 1 :
            self.DrawLineBehind(endX, endZ)
        else :
            self.DrawLine(endX, endZ)



    def DrawLeft(self, start, end, behind) :
        startX = start[0] * 5 - 100
        startZ = start[2] * 5
        endX = end[0] * 5 - 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        if behind == 1 :
            self.DrawLineBehind(endX, endZ)
        else :
            self.DrawLine(endX, endZ)


    def DrawTop(self, start, end, behind) :
        startX = -start[0] * 5 + 110
        startY = start[1] * 5
        endX = -end[0] * 5 + 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        if behind == 1 :
            self.DrawLineBehind(endY, endX)
        else :
            self.DrawLine(endY, endX)


    def DrawBottom(self, start, end, behind) :
        startX = start[0] * 5 - 110
        startY = start[1] * 5
        endX = end[0] * 5 - 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        if behind == 1 :
            self.DrawLineBehind(endY, endX)
        else :
            self.DrawLine(endY, endX)
