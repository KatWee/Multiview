import turtle
class Draw2D :

    def __init__(self, edges, verticies, surfaces):
        self.edges = edges
        self.verticies = verticies
        self.surfaces = surfaces
        self.t = turtle.Turtle()
        self.s = turtle.Screen()


    def show2D(self):
        self.s.title("2D")
        self.s.screensize(800,800,bg="white")

        self.t.pencolor("gray")
        self.t.pensize(3)
        self.t.speed(0)

        maxX, minX = self.FindMinMax(0)
        maxY, minY = self.FindMinMax(1)
        maxZ, minZ = self.FindMinMax(2)

        #draw behind line
        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]

            #front view
            self.DrawFront(start, end, 1)

            #back view
            self.DrawBack(start, end, 1)

            #right view
            self.DrawRight(start, end, 1)

            #left view
            self.DrawLeft(start, end, 1)

            #top view
            self.DrawTop(start, end, 1)

            #bottom view
            self.DrawBottom(start, end, 1)

        #find surface in each plane
        sameX = self.SurfaceView(0)
        sameY = self.SurfaceView(1)
        sameZ = self.SurfaceView(2)

        #sort suface from nearest
        frontSort = self.SortDept (minX, maxX, 0, sameX)
        backSort = frontSort[::-1]
        rightSort = self.SortDept (minY, maxY, 1, sameY)
        leftSort = rightSort[::-1]
        topSort = self.SortDept (minZ, maxZ, 2, sameZ)
        bottomSort = topSort[::-1]

        #find visible surface
        frontPlane = self.Isvisible(frontSort, 0, 1, 2, maxX)
        backPlane = self.Isvisible(backSort, 0, 1, 2, minX)
        rightPlane= self.Isvisible(rightSort, 1, 0, 2, maxY)
        leftPlane= self.Isvisible(leftSort, 1, 0, 2, minY)
        topPlane= self.Isvisible(topSort, 2, 1, 0, maxZ)
        bottomPlane= self.Isvisible(bottomSort, 2, 1, 0, minZ)

        self.t.pencolor("pink")
        for edge in self.edges:
            start = self.verticies[edge[0]]
            end = self.verticies[edge[1]]

            #front view
            if (self.IsinPlane(frontPlane, start) and
            self.IsinPlane(frontPlane, end)) :
                self.DrawFront(start, end, 0)

            #back view
            if (self.IsinPlane(backPlane, start) and
            self.IsinPlane(backPlane, end)) :
                self.DrawBack(start, end, 0)

            #right view
            if (self.IsinPlane(rightPlane, start) and
            self.IsinPlane(rightPlane, end)) :
                self.DrawRight(start, end, 0)

            # #left view
            if (self.IsinPlane(leftPlane, start) and
            self.IsinPlane(leftPlane, end)) :
                self.DrawLeft(start, end, 0)

            #top view
            if (self.IsinPlane(topPlane, start) and
            self.IsinPlane(topPlane, end)) :
                self.DrawTop(start, end, 0)

            #bottom view
            if (self.IsinPlane(bottomPlane, start) and
            self.IsinPlane(bottomPlane, end)) :
               self.DrawBottom(start, end, 0)

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


    def DrawLine(self, coor1, coor2) :
        self.t.pendown()
        self.t.goto(coor1, coor2)
        self.t.penup()


    def DrawFront(self, start, end, behind) :
        startY = start[1] * 5
        startZ = start[2] * 5
        endY = end[1] * 5
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        self.DrawLine(endY, endZ)


    def DrawBack(self, start, end, behind) :
        startY = -start[1] * 5 - 200
        startZ = start[2] * 5
        endY = -end[1] * 5 - 200
        endZ = end[2] * 5

        self.JumpTo(startY, startZ)
        self.DrawLine(endY, endZ)


    def DrawRight(self, start, end, behind) :
        startX = -start[0] * 5 + 100
        startZ = start[2] * 5
        endX = -end[0] * 5 + 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        self.DrawLine(endX, endZ)



    def DrawLeft(self, start, end, behind) :
        startX = start[0] * 5 - 100
        startZ = start[2] * 5
        endX = end[0] * 5 - 100
        endZ = end[2] * 5

        self.JumpTo(startX, startZ)
        self.DrawLine(endX, endZ)


    def DrawTop(self, start, end, behind) :
        startX = -start[0] * 5 + 110
        startY = start[1] * 5
        endX = -end[0] * 5 + 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        self.DrawLine(endY, endX)


    def DrawBottom(self, start, end, behind) :
        startX = start[0] * 5 - 110
        startY = start[1] * 5
        endX = end[0] * 5 - 110
        endY = end[1] * 5

        self.JumpTo(startY, startX)
        self.DrawLine(endY, endX)


    def SurfaceView(self, d) :
        plane = []
        samePlane = []
        for surface in self.surfaces :
            dept = self.verticies[surface[0]]
            for vertex in surface :
                thisVertex = self.verticies[vertex]
                if(dept[d] == thisVertex[d]) :
                    plane.append(thisVertex)
                else :
                    plane = []

            if plane != [] :
                samePlane.append(plane)
                plane = []

        return samePlane


    def SortDept (self, min, max, d,surface) :
        dept = max
        sort = []
        while dept >= min :
            for plane in surface :
                if plane[0][d] == dept :
                    sort.append(plane)
            dept -= 1

        return sort


    def FindLimitPlane (self, plane, w, h) :
        maxh = plane[0][h]
        minh = plane[0][h]
        maxw = plane[0][w]
        minw = plane[0][w]
        for vertex in plane :
            if maxh < vertex[h] :
                maxh = vertex[h]
            if minh > vertex[h] :
                minh = vertex[h]
            if maxw < vertex[w] :
                maxw = vertex[w]
            if minw > vertex[w] :
                minw = vertex[w]
        return [maxh, minh, maxw, minw]


    def Isvisible (self, surface, d, w, h, max) :
        visible = []
        limit = []
        for plane in surface :
            if plane[0][d] == max :
                vis = 1
            else :
                check = len(plane)
                for vertex in plane :
                    for lim in limit :
                        if( lim[0] >= vertex[h] and
                        lim[1] <= vertex[h] and
                        lim[2] >= vertex[w] and
                        lim[3] <= vertex[w] ) :
                            check -= 1

                if check <= 0 :
                    vis = 0
                else :
                    vis = 1

            if vis == 1 :
                minmax = self.FindLimitPlane (plane, w, h)
                limit.append(minmax)
                visible.append(plane)

        return visible


    def IsinPlane (self, surface, point) :
        for plane in surface :
            for vertex in plane :
                if point == vertex :
                    return 1