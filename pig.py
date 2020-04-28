class pig:
    def __init__(self):
        self.verticies = (
            (7, -7, -7), (7, 7, -7), (-7, -7, -7), (-7, 7, -7), #0, 1, 2, 3
            (7, -7, 7), (7, 7, 7), (-4 ,-7 ,7), (-4, -4, 7), #4, 5, 6, 7
            (-7, -4, 7), (-4, -7 ,10), (-4, -4 ,10), (-7 ,-7 ,10), #8, 9, 10, 11
            (-7, -4, 10), (-4, 4, 7), (-4, 7, 7), (-7, 4, 7), #12, 13, 14, 15
            (-4, 4, 10), (-4, 7, 10), (-7, 4, 10), (-7, 7, 10), #16, 17, 18, 19
            (9, -2, -2), (9, 2, -2), (7, -2, -2), (7, 2, -2), #20, 21, 22, 23
            (9, -2, 2), (9, 2, 2), (7, -2, 2), (7, 2, 2), #24, 25, 26, 27
            (-7, -7, 7), (-7, 7, 7), (9, -5, 3), (9, -3, 3), #28, 29, 30, 31
            (7, -5, 3), (7, -3, 3), (9, -5, 5), (9, -3, 5), #32, 33, 34, 35
            (7, -5, 5), (7, -3, 5), (9, 3, 3), (9, 5, 3), #36, 37, 38, 39
            (7, 3, 3), (7, 5, 3), (9, 3, 5), (9, 5, 5), #40, 41, 42, 43
            (7, 3, 5), (7, 5, 5) #44, 45
        )

        self.edges = (
            #head
            (0, 1), (0, 2), (0, 4),
            (1, 3), (1, 5),
            (2, 3), (2, 11),
            (3, 19),
            (4, 5), (4,6),
            (5, 14),
            #left ear
            (6, 7), (6, 9),
            (7, 10), (7, 8),
            (8, 12), (8, 15),
            (9, 10), (9, 11),
            (10, 12),
            (11, 12), (11, 28),
            #right ear
            (13, 14),(13, 15), (13,16),
            (14, 17),
            (15, 18),
            (16, 18), (16,17),
            (17, 19),
            (18, 19),
            (19, 29),
            #nose
            (20, 21), (20, 22), (20, 24),
            (21, 23), (21, 25),
            (22, 23), (22,26),
            (23, 27),
            (24, 25), (24, 26),
            (25, 27),
            (26, 27),
            #left eye
            (30, 31), (30, 32), (30, 34),
            (31, 33), (31, 35),
            (32, 33), (32, 36),
            (33,37),
            (34, 35), (34,36),
            (35, 37),
            (36, 37),
            #right eye
            (38, 39), (38, 40), (38, 42),
            (39, 41), (39, 43),
            (40, 41), (40, 44),
            (41, 45),
            (42, 43), (42, 44),
            (43, 45),
            (44, 45)
        )

        self.surfaces = (
            #head
            (0, 1, 4, 5), #front
            (2, 3, 28, 11, 12, 8, 15, 18, 19, 29), #back
            (1, 3, 5, 14, 17, 19, 29, 3), #right
            (0, 2, 4, 6, 9, 11, 28), #left
            (4, 5, 6, 7, 8, 15, 13, 14), #top
            (0, 1, 2, 3), #bottom
            #left ear
            (6, 7, 9, 10), #front
            (7, 8, 10, 12), #right
            (9, 10, 11, 12), #top
            #right ear
            (13, 14, 16, 17), #front
            (13, 15, 16, 18), #left
            (16, 17, 18, 19), #top
            #nose
            (20, 21, 24, 25), #front
            (21, 23, 25, 27), #right
            (20, 22, 24, 26), #left
            (24, 25, 26, 27), #top
            (20, 21, 22, 23), #bottom
            #left eye
            (30, 31, 34, 35), #front
            (31, 33, 35, 37), #right
            (30, 32, 34, 36), #left
            (34, 35, 36, 37), #top
            (30, 31, 32, 33), #bottom
            #right eye
            (38, 39, 42, 43), #front
            (39, 41, 43, 45), #right
            (38, 40, 42, 44), #left
            (42, 43, 44, 45), #top
            (38, 39, 40, 41) #bottom
        )