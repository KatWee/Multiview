import turtle
class Draw2D :

    def __init__(self, edges, verticies, surfaces):
        self.edges = edges
        self.verticies = verticies
        self.surfaces = surfaces
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

        ##draw behind line
        # for edge in self.edges:
        #     start = self.verticies[edge[0]]
        #     end = self.verticies[edge[1]]

        #     #front view
        #     self.DrawFront(start, end, 1)

        #     #back view
        #     self.DrawBack(start, end, 1)

        #     #right view
        #     self.DrawRight(start, end, 1)

        #     #left view
        #     self.DrawLeft(start, end, 1)

        #     #top view
        #     self.DrawTop(start, end, 1)

        #     #bottom view
        #     self.DrawBottom(start, end, 1)

        #draw nearest line
        sameX = self.SurfaceView(0)
        frontSort = self.SortDept (minX, maxX, 0, sameX)
        backSort = frontSort.reverse()
        sameY = self.SurfaceView(1)
        rightSort = self.SortDept (minY, maxY, 1, sameY)
        leftSort = rightSort.reverse()
        sameZ = self.SurfaceView(2)
        topSort = self.SortDept (minZ, maxZ, 2, sameZ)
        bottomSort = topSort.reverse()

        # front, back = self.Isvisible (sameX, 1, 2)
        # right, left = self.Isvisible (sameY, 0, 2)
        # top, bottom = self.Isvisible (sameZ, 1, 0)

        # for edge in self.edges:
        #     start = self.verticies[edge[0]]
        #     end = self.verticies[edge[1]]

        #     #front view
        #     if self.SelectEdge (front, start, end) :
        #         self.DrawFront(start, end, 0)

        #     #back view
        #     if self.SelectEdge (back, start, end) :
        #        self.DrawBack(start, end, 0)

        #     #right view
        #     if self.SelectEdge (right, start, end) :
        #         self.DrawRight(start, end, 0)

        #     # #left view
        #     if self.SelectEdge (left, start, end) :
        #         self.DrawLeft(start, end, 0)

        #     #top view
        #     if self.SelectEdge (top, start, end) :
        #         self.DrawTop(start, end, 0)

        #     #bottom view
        #     if self.SelectEdge (bottom, start, end) :
        #        self.DrawBottom(start, end, 0)


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


    def DrawLineBehind (self, coor1, coor2) :
        self.tBehind.pendown()
        self.tBehind.goto(coor1, coor2)
        self.tBehind.penup()


    # def Scan (self, minV, maxV, minH, maxH, d, v, h, near) :
    #     row = maxV
    #     list = []
    #     vertexList = []

    #     while row >= minV :
    #         col = minH
    #         while col <= maxH :

    #             for vertex in self.verticies :
    #                 if ( vertex[v] == row and
    #                 vertex[h] == col ) :
    #                     list.append(vertex)

    #             if list != [] :
    #                 vertexList.append(list)
    #                 list = []

    #             col += 1
    #         row -= 1

    #     visible = self.SelectVertex (vertexList, d, near)
    #     return visible


    # def SelectVertex (self, vertexList, d, near) :
    #     visible = []
    #     for list in vertexList :
    #         select = list[0]
    #         for vertex in list :
    #             if near == 1 :
    #                 if(select[d] < vertex[d]) :
    #                     select = vertex
    #             else :
    #                 if(select[d] > vertex[d]) :
    #                     select = vertex
    #         visible.append(select)

    #     return visible


    # def IsVisible(self,start, end, nearest, near, coord, coorv, coorh) :
    #     if self.IsNearest(coord, nearest, start, end) :
    #         print('top',start,end)
    #         return 1
    #     else :
    #         if self.IsNear(near, start, end, coord, coorv, coorh) :
    #             print('near',start,end)
    #             return 1
    #         else :
    #             return 0


    # def IsNearest(self, coor, nearest, start, end) :
    #     if (start[coor] == nearest and
    #     end[coor] == nearest) :
    #         return 1
    #     else :
    #         return 0


    # def IsNear(self, near, start, end, coord, coorv, coorh) :
    #     if near == 1 :
    #         maxS = self.FindNear(start, coorv, coorh, coord)
    #         maxE = self.FindNear(end, coorv, coorh, coord)
    #     else :
    #         maxS = self.FindDept(start, coorv, coorh, coord)
    #         maxE = self.FindDept(end, coorv, coorh, coord)

    #     if (start[coord] == maxS and
    #     end[coord] == maxE ) :
    #         return 1
    #     else :
    #         return 0



    # def FindNear(self, point, coorv, coorh, coord) :
    #     max = point[coord]
    #     for vertex in self.verticies :
    #         if (point[coorv] == vertex[coorv] and
    #         point[coorh] == vertex[coorh] ) :
    #             if vertex[coord] > max :
    #                 max = vertex[coord]
    #     return max


    # def FindDept(self, point, coorv, coorh, coord) :
    #     min = point[coord]
    #     for vertex in self.verticies :
    #         if (point[coorv] == vertex[coorv] and
    #         point[coorh] == vertex[coorh] ) :
    #             if vertex[coord] < min :
    #                 min = vertex[coord]
    #     return min


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


    def DrawPlane (self, start, end, near) :
        foundStart = 0
        foundEnd = 0
        for plane in near :
            for vertex in plane :
                if start == vertex :
                    foundStart = 1
                if end == vertex :
                    foundEnd = 1

        if(foundStart and foundEnd) :
            return 1
        else :
            return 0


    def SortDept (self, min, max, d,surface) :
        dept = max
        sort = []
        while dept >= min :
            for plane in surface :
                if plane[0][d] == dept :
                    sort.append(plane)
            dept -= 1

        return sort


    # def FindMinMaxPlane (self, surface, w, h) :
    #     maxh = surface[0][0][h]
    #     minh = surface[0][0][h]
    #     maxw = surface[0][0][w]
    #     minw = surface[0][0][w]
    #     for plane in surface :
    #         for vertex in plane :
    #             if maxh < vertex[h] :
    #                 maxh = vertex[h]
    #             if minh > vertex[h] :
    #                 minh = vertex[h]
    #             if maxw < vertex[w] :
    #                 maxw = vertex[w]
    #             if minw > vertex[w] :
    #                 minw = vertex[w]
    #     return maxh, minh, maxw, minw


    # def Isvisible (self, surface, w, h) :
    #     visible  = []
    #     invisible = []
    #     for vertex in surface[0]:
    #         visible.append(vertex)
    #     temp = len(visible)

    #     for plane in surface :
    #         for vertex in plane :
    #             if self.Isin(visible, vertex, w, h) == 0:
    #                 visible.append(vertex)
    #             else :
    #                 invisible.append(vertex)

    #     i=0
    #     while i <= temp :
    #         invisible.pop(i)
    #         i += 1

    #     return visible, invisible


    # def Isin (self, list, element, w, h) :
    #     for elem in list :
    #         if (elem[w] == element[w] and 
    #         elem[h] == element[h]):
    #             return 1
    #     return 0

    # def SelectEdge (self, visible, start, end) :
    #     foundStart = 0
    #     foundEnd = 0

    #     for vertex in visible :
    #         if vertex == start :
    #             foundStart = 1

    #     for vertex in visible :
    #         if vertex == end :
    #             foundEnd = 1

    #     if foundStart or foundEnd :
    #         return 1
    #     else :
    #         return 0