splitArr = []
triangleArr = []
rectArr = []

def splitted_add():
    splitArr.append([])
    print()
    print()
    
    print("Enter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        splitArr[len(splitArr) - 1].append(input())
    
    print(" --> ".join(splitArr[len(splitArr) - 1]))

def splitted_search():
    print()
    print()
    print("Enter searched stage: ")
    
    try:
        finded = splitArr[int(input()) - 1]

        print(" --> ".join(finded))
    except:
        print("Sorry, no index")

def splitted_show():
    print()
    print()
    for i in range(0, len(splitArr)):
        print("Index " + str(i+1) + ":")
        print(" --> ".join(splitArr[i]))

def new_splitted_arr():
    splitArr = []


    while (True):
        print()
        print()
        print("1 - Add")
        print("2 - Search")
        print("3 - Show")
        print("0 - Exit")

        match (int(input())):
            case 1:
                splitted_add()
                break
            case 2:
                splitted_search()
                break
            case 3:
                splitted_show()
                break
            case other:
                break        

def triangle_add():
    print()
    print()
    
    print("Enter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        if (i == 0):
            triangleArr.append([input()])
        else:
            triangleArr.append([*triangleArr[len(triangleArr) - 2], input()])

    print(" --> ".join(triangleArr[len(triangleArr) - 1]))

def triangle_show():
    print()
    print()
    print(" --> ".join(triangleArr))


def new_triangle_arr():
    triangleArr = []

    while (True):
        print()
        print()
        print("1 - Add")
        print("2 - Show")
        print("0 - Exit")

        match (int(input())):
            case 1:
                triangle_add()
                break
            case 2:
                triangle_show()
                break
            case other:
                break

def rect_add():
    tempvar = []
    print()
    print()

    print("Enter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        tempvar.append(input())
    
    rectArr.append(tempvar)

    print(" --> ".join(rectArr[len(rectArr) - 1]))

def rect_search():
    print()
    print()
    print("Enter searched stage: ")
    
    try:
        finded = rectArr[int(input()) - 1]

        print(" --> ".join(finded))
    except:
        print("Sorry, no index")

def rect_show():
    print()
    print()
    for i in range(0, len(rectArr)):
        print("Index " + str(i+1) + ":")
        print(" --> ".join(rectArr[i]))


def new_rect_arr():
    rectArr = []

    while (True):
        print()
        print()
        print("1 - Add")
        print("2 - Search")
        print("3 - Show")
        print("0 - Exit")

        match (int(input())):
            case 1:
                rect_add()
                break
            case 2:
                rect_search()
                break
            case 3:
                rect_show()
            case other:
                break

while (True):
    print()
    print()
    print("Pick one")
    print("1 - Split array")
    print("2 - Triangle array")
    print("3 - Rect array")
    print("0 - Exit")

    match (int(input())):
        case 1:
            new_splitted_arr()
        case 2:
            new_triangle_arr()
        case 3:
            new_rect_arr()
        case other:
            break
