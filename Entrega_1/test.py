import random as r

def generatePoint(zone):
    if zone == 1:
        point = (r.randint(-75, 75), r.randint(-75, 75))

    elif zone == 2:
        x = r.randint(-300, 300)
        if (abs(x) > 75):
            y = r.randint(-300, 300)
        else:
            y = r.randint(*r.choice([(-300, -76),(76, 300)]))
        point = (x, y)

    return point
    


def generateInstancePoints(I, J):
    warehouses = []
    shops = []
    for i in range(I):
        while True:
            pointI = generatePoint(2)
            
            if pointI not in warehouses:
                warehouses.append(pointI)
                break
            continue
    
    for j in range(J):
        while True:
            pointJ = generatePoint(1)

            if pointJ not in shops:
                shops.append(pointJ)
                break
            continue

    return (warehouses, shops)



def main():
    print("            1          |          2          |           3           |")
    print("   |     Pequeñas      |      Medianas       |        Grandes        |")
    print("   |    I    |    J    |    I    |     J     |     I     |     J     |")
    print(" 1 |  5 - 7  |  6 - 10 | 32 - 38 |  50 - 65  |  72 - 81  | 125 - 145 |")
    print(" 2 |  8 - 12 | 10 - 20 | 39 - 45 |  65 - 80  |  82 - 91  | 145 - 165 |")
    print(" 3 | 13 - 18 | 20 - 30 | 46 - 53 |  80 - 95  |  92 - 101 | 165 - 185 |")
    print(" 4 | 19 - 23 | 30 - 40 | 54 - 65 |  95 - 110 | 102 - 111 | 185 - 205 |")
    print(" 5 | 24 - 30 | 40 - 50 | 66 - 72 | 110 - 125 | 112 - 131 | 205 - 225 |")


    while True:
        size = input("Tamaño de instancia (1, 2, 3):")
        if size in [1, 2, 3]:
            instNum = input("Número de instancia (1 - 5)")

    I = r.randint(5, 7)
    J = r.randint(6, 10)
    
    tup = generateInstancePoints(I, J)

    warehouses = tup[0]
    shops = tup[1]

    print(warehouses)
    print(shops)

    return

if __name__ == "__main__":
    main()











    """    
    print("            1          |          2          |           3           |")
    print("   |     Pequeñas      |      Medianas       |        Grandes        |")
    print("   |    I    |    J    |    I    |     J     |     I     |     J     |")
    print(" 1 |  5 - 7  |  6 - 10 | 32 - 38 |  50 - 65  |  72 - 81  | 125 - 145 |")
    print(" 2 |  8 - 12 | 10 - 20 | 39 - 45 |  65 - 80  |  82 - 91  | 145 - 165 |")
    print(" 3 | 13 - 18 | 20 - 30 | 46 - 53 |  80 - 95  |  92 - 101 | 165 - 185 |")
    print(" 4 | 19 - 23 | 30 - 40 | 54 - 65 |  95 - 110 | 102 - 111 | 185 - 205 |")
    print(" 5 | 24 - 30 | 40 - 50 | 66 - 72 | 110 - 125 | 112 - 131 | 205 - 225 |")


     while True:
        size = input("Tamaño de instancia (1, 2, 3):")
        if size in [1, 2, 3]:
            instNum = input("Número de instancia (1 - 5)")
            if instNum in range(1, 6):
                match size:
                    case 1:
                        match instNum:
                            case 1:
                                print(f"Bodegas: {}") """