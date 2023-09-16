import random as r

# INSTANCES_S = []
# INSTANCES_M = []
# INSTANCES_L = []
INSTANCES = [[], [], []]
ZONES = ["Verde Oscuro", "Verde Claro", "Azul"]
RANGES = [
    [(5, 7), (6, 10)], [(8, 12), (10, 20)], [(13, 18), (20, 30)], [(19, 23), (30, 40)], [(24, 30), (40, 50)],
    [(32, 38), (50, 65)], [(39, 45), (65, 80)], [(46, 53), (80, 95)], [(54, 65), (95, 110)], [(66, 72), (110, 125)], 
    [(72, 81), (125, 145)], [(82, 91), (145, 165)], [(92, 101), (165, 185)], [(102, 111), (185, 205)], [(112, 131), (205, 225)]]

def generatePoint(zone):
    if zone == 0:
        point = (r.randint(-75, 75), r.randint(-75, 75), zone)

    elif zone == 1:
        x = r.randint(-200, 200)
        if (abs(x) > 75):
            y = r.randint(-200, 200)
        else:
            y = r.randint(*r.choice([(-200, -76),(76, 200)]))
        point = (x, y, zone)

    elif zone == 2:
        x = r.randint(-300, 300)
        if (abs(x) > 200):
            y = r.randint(-300, 300)
        else:
            y = r.randint(*r.choice([(-300, -201), (201, 300)]))
        point = (x, y, zone)

    return point


def distance(point1, point2):
    """ Calcula la distancia entre dos puntos """
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5)


def createDistanceMatrix(I, J):
    distances = []
    for i, itemI in enumerate(I):
        distances.append([])
        for _, itemJ in enumerate(J):
            distances[i].append(distance(itemI, itemJ))
    return distances


def generate(it):

    I = []
    J = []
    distances = []

    for _ in range(r.randint(*RANGES[it - 1][0])):
        while True:
            # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
            point = generatePoint(r.choice([1, 2]))
            if point not in I:
                I.append(point)
                distances.append([])
                break
            continue

    for _ in range(r.randint(*RANGES[it - 1][0])):
        while True:
            # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
            point = generatePoint(0)
            if point not in J:
                J.append(point)
                break
            continue
    distances = createDistanceMatrix(I, J)

    instances = [I, J, distances]

    return instances


def main():

    for i in range(1, 6):
        # Se generan las 15 instancias a la vez
        INSTANCES[0].append(generate(i))
        INSTANCES[1].append(generate(5 + i))
        INSTANCES[2].append(generate(10 + i))
    
    print("            1          |          2          |           3           |")
    print("   |      Pequeñas     |      Medianas       |        Grandes        |")
    print("   |    I    |    J    |    I    |     J     |     I     |     J     |")
    print(" 1 |  5 - 7  |  6 - 10 | 32 - 38 |  50 - 65  |  72 - 81  | 125 - 145 |")
    print(" 2 |  8 - 12 | 10 - 20 | 39 - 45 |  65 - 80  |  82 - 91  | 145 - 165 |")
    print(" 3 | 13 - 18 | 20 - 30 | 46 - 53 |  80 - 95  |  92 - 101 | 165 - 185 |")
    print(" 4 | 19 - 23 | 30 - 40 | 54 - 65 |  95 - 110 | 102 - 111 | 185 - 205 |")
    print(" 5 | 24 - 30 | 40 - 50 | 66 - 72 | 110 - 125 | 112 - 131 | 205 - 225 |")


    while True:
        size = int(input("Tamaño de instancia (1, 2, 3): "))
        if size in [1, 2, 3]:
            instNum = int(input("Número de instancia (1 - 5): "))
            if instNum in range(1, 6):
                
                JQuant = len(INSTANCES[size - 1][instNum - 1][1])
                k = 0
                while (k < len(INSTANCES[size - 1][instNum - 1][0])):

                    capacity = r.randint(2, round(JQuant/3))
                    print(f"\t({INSTANCES[size - 1][instNum - 1][0][k][0]}, {INSTANCES[size - 1][instNum - 1][0][k][1]}) | {ZONES[INSTANCES[size - 1][instNum - 1][0][k][2]]}")
                    print(f"\tCosto de instalación: {r.randint(1000, 3000)} | Emisiones por operación: {r.randint(20, 70)} | Capacidad: {capacity}")
                    
                    t = 0
                    while (t < JQuant):
                        dist = INSTANCES[size - 1][instNum - 1][2][k][t]
                        print(f"\t\tDistancia con respecto a tienda en ({INSTANCES[size - 1][instNum - 1][1][t][0]}, {INSTANCES[size - 1][instNum - 1][1][t][1]}): {dist} | Costo de transporte: {1.25 * dist} | Emisiones: {1.5 * dist}")
                        t += 1

                    k += 1
                    print("")
                break
        continue

    return 0


if __name__ == "__main__":
    main()