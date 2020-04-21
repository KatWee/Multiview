from Draw3D import Draw3D
from Draw2D import Draw2D

verticies = (
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

edges = (
    #head
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 11),
    (3, 19),
    (4, 5), (4,6),
    (5, 14),
    #left ear
    (6, 7), (6, 9),
    (7, 10), (7,8),
    (8,12), (8,15),
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


def main():
    print("===================================")
    print("Welcome to Multi-View Program")
    print("1 : show 3D model")
    print("2 : show Multi-View")
    print("Press others numbers key to exit")
    print("===================================")

    while True:
        try:
            userin = int(input("select > "))
            break
        except ValueError:
            print("Invalid input : Please Input Number")

    if userin == 1:
        d3 = Draw3D(edges, verticies)
        d3.show3D()
    elif userin == 2:
        d2 = Draw2D(edges, verticies)
        d2.show2D()
    else :
        print("Exit Program")

main()