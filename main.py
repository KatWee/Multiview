from Draw3D import Draw3D
from Draw2D import Draw2D
from pig import pig

def main():
    pic = pig()
    print("===================================")
    print("Welcome to Multi-View Program")
    print("1 : show 3D model")
    print("2 : show Multi-View")
    print("Press others numbers key to exit")
    print("===================================")

    #check if input is not number user have to input again
    while True:
        try:
            userin = int(input("select > "))
            break
        except ValueError:
            print("Invalid input : Please Input Number")

    #input is 1 -> draw 3D
    if userin == 1:
        d3 = Draw3D(pic.edges, pic.verticies)
        d3.show3D()
    #input is 2 -> draw multiview
    elif userin == 2:
        d2 = Draw2D(pic.edges, pic.verticies, pic.surfaces)
        d2.show2D()
    #input is any number exit program
    else :
        print("Exit Program")

main()