import random as r

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

    I = sorted(I, key=lambda x: x[2], reverse=True)
    J = sorted(J, key=lambda x: x[2], reverse=True)
    instance = [I, J, distances]

    return instance


def getResults(instance):
    """
    Modela el problema con los datos generados, genera un string para mostrar en pantalla.
 
    Args:
        size (int): El tamaño de la instancia (1: Pequeña, 2: Mediana, 3: Grande).
        insNum (int): Número de instancia dentro del tamaño (1 - 5).
 
    Returns:
        tuple: (Valor de J, String que describe el modelo).
    """ 
    JQuant = len(instance[1])
    outputString = ""
    k = 0
    for i, point in enumerate(instance[1]):
        print(f"J{i + 1}: ({point[0]}, {point[1]})")
    while k < len(instance[0]):

        capacity = r.randint(2, round(JQuant/3))
        installCost = r.randint(1000, 3000)
        opEmissions = r.randint(20, 70)
        outputString += (f"\nG.{k + 1}.{'B' if (instance[0][k][2] == 1) else 'A'}: {installCost}\nC.{k + 1}.{'B' if (instance[0][k][2] == 1) else 'A'}: {opEmissions}\nK.{k + 1}.{'B' if (instance[0][k][2] == 1) else 'A'}: {capacity}")
        G.append(('B' if (instance[0][k][2] == 1) else 'A', installCost))
        C.append(('B' if (instance[0][k][2] == 1) else 'A', opEmissions))
        K.append(('B' if (instance[0][k][2] == 1) else 'A', capacity))
        
        t = 0
        Di = []
        while t < JQuant:
            dist = instance[2][k][t]
            outputString += (f"\nD.{k + 1}.{t + 1}: {dist}")
            Di.append(dist)
            t += 1
        D.append(Di)
        k += 1
        outputString += ("\n;")
    return (JQuant, outputString)


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
                match size:
                    case 1:
                        return instNum - 1
                    case 2:
                        return 4 + (instNum - 1)
                    case 3:
                        return 9 + (instNum - 1)
                
        continue


def main():
    size = chooseInstanceSize()
    instance = generate(size)
    results = getResults(instance)
    LPout = aux2 = ""
    aux1 = "min: "
    for x, value in enumerate(C):
        aux1 += f"{value[1]} B{x + 1}{value[0]} + "
        for y, item in enumerate(D[x]):
            aux2 += f"{item * 1.5} Y{x + 1}a{y + 1}{value[0]} + "

    LPout += aux1 + aux2[:-3] + ";\n"
    aux1 = aux2 = ""
    
    for k, item in enumerate(D):
        if G[k][0] == 'A':
            for m, _ in enumerate(item):
                aux1 += f"Y{k + 1}a{m + 1}{G[k][0]} + "
            aux1 = aux1[:-2] + f"<= {RANGES[size][0][1] * RANGES[size][1][1]} B{k + 1}{G[k][0]};\n"

        elif G[k][0] == 'B':
            for n, _ in enumerate(item):
                aux1 += f"Y{k + 1}a{n + 1}{G[k][0]} + "
            aux1 = aux1[:-2] + f"<= {RANGES[size][0][1] * RANGES[size][1][1]} B{k + 1}{G[k][0]};\n"

    LPout += aux1
    aux1 = ""

    for i, item in enumerate(G):
        aux1 += f"{item[1]} B{i + 1}{item[0]} + "

        for j, item in enumerate(D[i]):
            aux2 += f"{item * 1.25} Y{i + 1}{j + 1}{C[i][0]} + "
   
    aux2 = aux2[:-3]
   
    LPout += aux1 + aux2 + f" <= {6000 * results[0]};\n"

    aux1 = aux2 = ""

    for j in range(results[0]):
        for i, item in enumerate(C):
            aux1 += f"Y{i + 1}a{j + 1}{item[0]} + "
        aux1 = aux1[:-2] + "= 1;\n"

    LPout += aux1

    aux1 = aux3 = ""

    countA = countB = 0
    for k, item in enumerate(G):
        
        if item[0] == 'A':
            countA += 1
            aux2 += f"B{k + 1}A + "
            for m, value in enumerate(D[k]):
                aux1 += f"Y{k + 1}a{m + 1}A + "
            aux1 = aux1[:-2] + f"<= {K[k][1]};\n"
        
        elif item[0] == 'B':
            countB += 1
            aux3 += f"B{k + 1}B + "
            for n, value in enumerate(D[k]):
                aux1 += f"Y{k + 1}a{n + 1}B + "
            aux1 = aux1[:-2] + f"<= {K[k][1]};\n"

    aux2 = aux2[:-2] + f">= {int(countA * 0.4)};\n"
    aux3 = aux3[:-2] + f">= {int(countB * 0.4)};\n"
    LPout += aux1 + f"{aux2 if countA > 0 else ''}" + f"{aux3 if countB > 0 else ''}"

    aux1 = "bin "
    aux2 = ""

    for i, item in enumerate(C):
        aux2 += f"B{i + 1}{item[0]}, "
        for j in range(results[0]):
            aux1 += f"Y{i + 1}a{j + 1}{item[0]}, "

    LPout += aux1 + aux2[:-2] +  ";"

    with open("LPModel.lp", "w", encoding="utf8") as file:
        file.write(LPout)

    print(LPout)

    return 0


if __name__ == "__main__":
    main()
