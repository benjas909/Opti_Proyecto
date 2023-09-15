import random as r

INSTANCES_S = []
INSTANCES_M = []
INSTANCES_L = []
INSTANCES = [INSTANCES_S, INSTANCES_M, INSTANCES_L]
ZONAS = ["Verde Oscuro", "Verde Claro", "Azul"]


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


def createDistanceMatrix(Ilist, Jlist):
    distances = []
    for i in range(len(Ilist)):
        distances.append([])
        for j in range(len(Jlist)):
            distances[i].append(distance(Ilist[i], Jlist[j]))
    return distances


def generateS(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    distances = []
    match it:
        case 1:
            
            iQuant = r.randint(5, 7)
            for _ in range(iQuant): # Elige un número aleatorio en el rango dado
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            jQuant = r.randint(6, 10)
            for _ in range(jQuant):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 2:
            
            for _ in range(r.randint(8, 12)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(10, 20)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 3:
        
            for _ in range(r.randint(13, 18)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos 
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(20, 30)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

        case 4:
            
            for _ in range(r.randint(19, 23)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(30, 40)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 5:
            
            for _ in range(r.randint(24, 30)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(40, 50)):
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
    

def generateM(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    distances = []
    match it:
        case 1:

            for _ in range(r.randint(32, 38)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(50, 65)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

        
        case 2:
            
            for _ in range(r.randint(39, 45)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(65, 80)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 3:
        
            for _ in range(r.randint(46, 53)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(80, 95)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

        case 4:

            for _ in range(r.randint(54, 65)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(95, 110)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 5:

            for _ in range(r.randint(66, 72)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(110, 125)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

    instances = [I, J, distances]

    return instances


def generateL(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    distances = []
    match it:
        case 1:
            
            for _ in range(r.randint(72, 81)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(125, 145)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 2:
            
            for _ in range(r.randint(82, 91)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(145, 165)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 3:
        
            for _ in range(r.randint(92, 101)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(165, 185)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

        case 4:

            for _ in range(r.randint(102, 111)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(185, 205)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)
        
        case 5:

            for _ in range(r.randint(112, 131)):
                while True:
                        
                    point = generatePoint(r.choice([1, 2]))
                    if point not in I:
                        I.append(point)
                        distances.append([])
                        break
                    continue
            
            for _ in range(r.randint(205, 225)):
                while True:

                    point = generatePoint(0)
                    if point not in J:
                        J.append(point)
                        break
                    continue
            distances = createDistanceMatrix(I, J)

    instances = [I, J, distances]

    return instances


def distance(point1, point2):
    """ Calcula la distancia entre dos puntos """
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5)


def main():

    for i in range(1, 6):
        # Se generan las 15 instancias a la vez
        INSTANCES_S.append(generateS(i))
        INSTANCES_M.append(generateM(i))
        INSTANCES_L.append(generateL(i))
    
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
                    print(f"\t({INSTANCES[size - 1][instNum - 1][0][k][0]}, {INSTANCES[size - 1][instNum - 1][0][k][1]}) | {ZONAS[INSTANCES[size - 1][instNum - 1][0][k][2] - 1]}")
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