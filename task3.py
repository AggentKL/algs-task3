import time
import sys as sus

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

splitArr = []
triangleArr = []
rectArr = []

def splitted_add():
    splitArr.append([])
    print("\n\nEnter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        splitArr[len(splitArr) - 1].append(input())
    
    print(" --> ".join(splitArr[len(splitArr) - 1]))
    print(f"Memory occupied: {sus.getsizeof(splitArr)} bytes")

def splitted_search():
    print("\n\nEnter searched stage: ")
    
    try:
        start_time = time.time()
        finded = splitArr[int(input()) - 1]
        end_time = time.time()
        time_lapsed = end_time - start_time
        print("Finded stage:")
        print(" --> ".join(finded))
        time_convert(time_lapsed)

    except:
        print("Sorry, invalide index")

def splitted_show():
    for i in range(0, len(splitArr)):
        print("\n\nIndex " + str(i+1) + ":")
        print(" --> ".join(splitArr[i]))

def new_splitted_arr():
    splitArr = []


    while (True):
        print("\n\n1 - Add")
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
    print("\n\nEnter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        if (i == 0):
            triangleArr.append([input()])
        else:
            triangleArr.append([*triangleArr[len(triangleArr) - 2], input()])

    print(" --> ".join(triangleArr[len(triangleArr) - 1]))
    print(f"Memory occupied: {sus.getsizeof(triangleArr)} bytes")

def triangle_search():
    print("\n\nEnter searched stage: ")
    
    try:
        start_time = time.time()
        finded = triangleArr[int(input()) - 1]
        end_time = time.time()
        time_lapsed = end_time - start_time
        print("Finded stage:")
        print(" --> ".join(finded))
        time_convert(time_lapsed)

    except:
        print("Sorry, invalide index")

def triangle_show():
    print("\n\n --> ".join(triangleArr))


def new_triangle_arr():
    triangleArr = []

    while (True):
        print("\n\n1 - Add")
        print("2 - Search")
        print("3 - Show")
        print("0 - Exit")

        match (int(input())):
            case 1:
                triangle_add()
                break
            case 2:
                triangle_search()
                break
            case 3:
                triangle_show()
                break
            case other:
                break

def rect_add():
    tempvar = []
    print("\n\nEnter count of stages")
    stages = int(input())

    for i in range(0, stages):
        print("Enter " + str(i+1) + " stage: ")
        tempvar.append(input())
    
    rectArr.append(tempvar)

    print(" --> ".join(rectArr[len(rectArr) - 1]))
    print(f"Memory occupied: {sus.getsizeof(rectArr)} bytes")

def rect_search():
    print("\n\nEnter searched stage: ")
    
    try:
        start_time = time.time()
        finded = rectArr[int(input()) - 1]
        end_time = time.time()
        time_lapsed = end_time - start_time
        print("Finded stage:")
        print(" --> ".join(finded))
        time_convert(time_lapsed)
    except:
        print("Sorry, invalide index")

def rect_show():
    print()
    print()
    for i in range(0, len(rectArr)):
        print("Index " + str(i+1) + ":")
        print(" --> ".join(rectArr[i]))


def new_rect_arr():
    rectArr = []

    while (True):
        print("\n\n1 - Add")
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
    print("\n\nPick one")
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
