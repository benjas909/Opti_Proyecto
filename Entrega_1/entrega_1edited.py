import random as r

INSTANCES = [[], [], []]
ZONES = ["Verde Oscuro", "Verde Claro", "Azul"]
RANGES = [
    [(5, 7), (6, 10)], [(8, 12), (10, 20)], [(13, 18), (20, 30)],
    [(19, 23), (30, 40)], [(24, 30), (40, 50)],[(32, 38), (50, 65)],
    [(39, 45), (65, 80)], [(46, 53), (80, 95)], [(54, 65), (95, 110)],
    [(66, 72), (110, 125)], [(72, 81), (125, 145)], [(82, 91), (145, 165)],
    [(92, 101), (165, 185)], [(102, 111), (185, 205)], [(112, 131), (205, 225)]
    ]
C = []
G = []
K = []
D = []

def generatePoint(zone):
    """ Genera una 3-tupla con las coordenadas x e y del punto, además de el número de zona"""
    if zone == 0:
        point = (r.randint(-75, 75), r.randint(-75, 75), zone)

    elif zone == 1:
        x = r.randint(-200, 200)
        if abs(x) > 75:
            # Si se cumple, significa que el punto está en uno de los dos lados del cuadrado
            y = r.randint(-200, 200)
        else:
            # Si no, está arriba o abajo, por lo tanto debemos generar la coordenada y en una de las dos zonas
            y = r.randint(*r.choice([(-200, -76),(76, 200)]))
        point = (x, y, zone)

    elif zone == 2:
        x = r.randint(-300, 300)
        if abs(x) > 200:
            # Si se cumple, significa que el punto está en uno de los dos lados del cuadrado
            y = r.randint(-300, 300)
        else:
            # Si no, está arriba o abajo, por lo tanto debemos generar la coordenada y en una de las dos zonas
            y = r.randint(*r.choice([(-300, -201), (201, 300)]))
        point = (x, y, zone)

    return point


def distance(point1, point2):
    """ Calcula la distancia entre dos puntos """
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5)


def createDistanceMatrix(I, J):
    """  Crea una matriz de la forma I x J con las distancias entre el los puntos I y los puntos J de la instancia """
    distances = []
    for i, itemI in enumerate(I):
        distances.append([])
        for itemJ in J:
            distances[i].append(distance(itemI, itemJ))
    return distances


def generate(it):
    """ Genera una lista que contiene una lista de puntos I, una de puntos J, 
    y la matriz de distancias entre ambos grupos de coordenadas"""
    I = []
    J = []
    distances = []

    for _ in range(r.randint(*RANGES[it][0])):
        while True:
            # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
            point = generatePoint(r.choice([1, 2]))
            if point not in I:
                I.append(point)
                distances.append([])
                break
            continue

    for _ in range(r.randint(*RANGES[it][1])):
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

def generateAllInstances():
    for i in range(5):
        # Se generan las 15 instancias a la vez
        INSTANCES[0].append(generate(i))
        INSTANCES[1].append(generate(4 + i))
        INSTANCES[2].append(generate(9 + i))
    return


def getResults(size, instNum):
    JQuant = len(INSTANCES[size - 1][instNum - 1][1])
    outputString = ""
    k = 0
    for i in range(len(INSTANCES[size - 1][instNum - 1][1])):
        print(f"J{i + 1}: ({INSTANCES[size - 1][instNum - 1][1][i][0]}, {INSTANCES[size - 1][instNum - 1][1][i][1]})")
    while (k < len(INSTANCES[size - 1][instNum - 1][0])):

        capacity = r.randint(2, round(JQuant/3))
        # outputString += (f"\n\t({INSTANCES[size - 1][instNum - 1][0][k][0]}, {INSTANCES[size - 1][instNum - 1][0][k][1]}) | {ZONES[INSTANCES[size - 1][instNum - 1][0][k][2]]}")
        installCost = r.randint(1000, 3000)
        opEmissions = r.randint(20, 70)
        outputString += (f"\nG.{k + 1}.{'B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A'}: {installCost}\nC.{k + 1}.{'B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A'}: {opEmissions}\nK.{k + 1}.{'B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A'}: {capacity}")
        G.append(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', installCost))
        C.append(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', opEmissions))
        K.append(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', capacity))
        print(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', installCost))
        print(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', opEmissions))
        print(('B' if (INSTANCES[size - 1][instNum - 1][0][k][2] == 1) else 'A', capacity))
        
        t = 0
        Di = []
        while (t < JQuant):
            
            dist = INSTANCES[size - 1][instNum - 1][2][k][t]
            outputString += (f"\nD.{k + 1}.{t + 1}: {dist}")
            Di.append(dist)
            t += 1
        D.append(Di)
        k += 1
        outputString += ("\n;")
    return outputString

def chooseInstanceSize():

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
                return (size, instNum)
                
        continue

def main():
    generateAllInstances()
    size = chooseInstanceSize()
    output = getResults(*size)
    LPout = ""
    lpc = "min: "
    lpd = ""
    for x in range(len(C)):
        lpc += f"{C[x][1]} B{x + 1}{C[x][0]} + "
        # print(len(D[x]))
        for y in range(len(D[x])):
            lpd += f"Y{x + 1}{y + 1} ({D[x][y]} * 1.5){';' if x == len(C) - 1 else ' + '}"
    LPout += lpc + lpd

    print(output)
    print(LPout)
    return 0


if __name__ == "__main__":
    main()