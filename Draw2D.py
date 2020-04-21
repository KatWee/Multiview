import turtle
class Draw2D :

    def __init__(self, edges, verticies):
        self.edges = edges
        self.verticies = verticies
        self.t = turtle.Turtle()
        self.s = turtle.Screen()


    def show2D(self):
        self.s.title("2D")
        self.s.screensize(800,800,bg="white")
        self.t.pencolor("black")
        self.t.pensize(3)
        self.t.speed(0)

        maxX, minX = self.FindMinMax(0)
        maxY, minY = self.FindMinMax(1)
        maxZ, minZ = self.FindMinMax(2)

        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]

            #front view
            self.DrawFront(start, end)

            #right view
            self.DrawRight(start, end)

            #left view
            self.DrawLeft(start, end)

            #top view
            self.DrawTop(start, end)

            #bottom view
            self.DrawBottom(start, end)

            #back view
            self.DrawBack(start, end)

        self.t.hideturtle()
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
        self.t.penup()
        self.t.goto(coor1, coor2)


    def DrawPlane(self, coor1, coor2) :
        self.t.pendown()
        self.t.goto(coor1, coor2)
        self.t.penup()


    def DrawFront(self, start, end) :
        startY = start[1] * 5
        startZ = start[2] * 5
        endY = end[1] * 5
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        self.DrawPlane(endY, endZ)


    def DrawRight(self, start, end) :
        startX = -start[0] * 5 + 100
        startZ = start[2] * 5
        endX = -end[0] * 5 + 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        self.DrawPlane(endX, endZ)


    def DrawLeft(self, start, end) :
        startX = start[0] * 5 - 100
        startZ = start[2] * 5
        endX = end[0] * 5 - 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        self.DrawPlane(endX, endZ)


    def DrawTop(self, start, end) :
        startX = -start[0] * 5 + 110
        startY = start[1] * 5
        endX = -end[0] * 5 + 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        self.DrawPlane(endY, endX)


    def DrawBottom(self, start, end) :
        startX = start[0] * 5 - 110
        startY = start[1] * 5
        endX = end[0] * 5 - 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        self.DrawPlane(endY, endX)


    def DrawBack(self, start, end) :
        startY = -start[1] * 5 - 200
        startZ = start[2] * 5
        endY = -end[1] * 5 - 200
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        self.DrawPlane(endY, endZ)