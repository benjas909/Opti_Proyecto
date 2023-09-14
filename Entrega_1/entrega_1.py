import random as r

INSTANCES_S = []
INSTANCES_M = []
INSTANCES_L = []



def generateS(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    match it:
        case 1:
            
            for _ in range(r.randint(5, 7)): # Elige un número aleatorio en el rango dado
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(6, 10)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 2:
            
            for _ in range(r.randint(8, 12)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(10, 20)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 3:
        
            for _ in range(r.randint(13, 18)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos 
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(20, 30)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

        case 4:
            
            for _ in range(r.randint(19, 23)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(30, 40)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 5:
            
            for _ in range(r.randint(24, 30)):
                while True:
                    # Si el punto no está en la lista I, se agrega, en caso contrario, se siguen generando puntos
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(40, 50)):
                while True:
                    # Si el punto no está en la lista J, se agrega, en caso contrario, se siguen generando puntos
                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

    instances = {"I": I, "J": J}

    return instances
    

def generateM(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    match it:
        case 1:

            for _ in range(r.randint(32, 38)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(50, 65)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 2:
            
            for _ in range(r.randint(39, 45)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(65, 80)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 3:
        
            for _ in range(r.randint(46, 53)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(80, 95)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

        case 4:

            for _ in range(r.randint(54, 65)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(95, 110)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 5:

            for _ in range(r.randint(66, 72)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(110, 125)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

    instances = {"I": I, "J": J}

    return instances


def generateL(it):
    """ Genera los puntos de bodegas y tiendas para las 5 instancias pequeñas """
    I = []
    J = []
    match it:
        case 1:
            
            for _ in range(r.randint(72, 81)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(125, 145)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 2:
            
            for _ in range(r.randint(82, 91)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(145, 165)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 3:
        
            for _ in range(r.randint(92, 101)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(165, 185)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

        case 4:

            for _ in range(r.randint(102, 111)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(185, 205)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 5:

            for _ in range(r.randint(112, 131)):
                while True:
                        
                    x = r.randint(-300, 300)
                    if (abs(x) > 75):
                        y = r.randint(-300, 300)
                    else:
                        y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                    if (x, y) not in I:
                        I.append((x, y))
                        break
                    
                    continue
            
            for _ in range(r.randint(205, 225)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

    instances = {"I": I, "J": J}

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
                JQuant = len(INSTANCES_S[instNum - 1]['J']) 
                match size:
                    case 1:

                        k = 0
                        while (k < len(INSTANCES_S[instNum - 1]['I'])):

                            capacity = r.randint(2, round(JQuant/3))
                            print(f"\t{INSTANCES_S[instNum - 1]['I'][k]}")
                            print(f"\tCosto de instalación: {r.randint(1000, 3000)} | Emisiones por operación: {r.randint(20, 70)} | Capacidad: {capacity}")
                            
                            t = 0
                            while (t < JQuant):
                                dist = distance(INSTANCES_S[instNum - 1]['I'][k], INSTANCES_S[instNum - 1]['J'][t])
                                print(f"\t\tDistancia con respecto a tienda en {INSTANCES_S[instNum - 1]['J'][t]}: {dist} | Costo de transporte: {1.25 * dist} | Emisiones: {1.5 * dist}")
                                t += 1

                            k += 1

                            print("")

                        break

                    case 2:
                        k = 0
                        while (k < len(INSTANCES_M[instNum - 1]['I'])):

                            capacity = r.randint(2, round(JQuant/3))
                            print(f"\t{INSTANCES_M[instNum - 1]['I'][k]}")
                            print(f"\tCosto de instalación: {r.randint(1000, 3000)} | Emisiones por operación: {r.randint(20, 70)} | Capacidad: {capacity}")
                            
                            t = 0
                            while (t < JQuant):
                                dist = distance(INSTANCES_M[instNum - 1]['I'][k], INSTANCES_M[instNum - 1]['J'][t])
                                print(f"\t\tDistancia con respecto a tienda en {INSTANCES_M[instNum - 1]['J'][t]}: {dist} | Costo de transporte: {1.25 * dist} | Emisiones: {1.5 * dist}")
                                t += 1

                            k += 1

                            print("")

                        break

                    case 3:
                        k = 0
                        while (k < len(INSTANCES_L[instNum - 1]['I'])):

                            capacity = r.randint(2, round(JQuant/3))
                            print(f"\t{INSTANCES_L[instNum - 1]['I'][k]}")
                            print(f"\tCosto de instalación: {r.randint(1000, 3000)} | Emisiones por operación: {r.randint(20, 70)}")

                            t = 0
                            while (t < JQuant):
                                dist = distance(INSTANCES_L[instNum - 1]['I'][k], INSTANCES_L[instNum - 1]['J'][t])
                                print(f"\t\tDistancia con respecto a tienda en {INSTANCES_L[instNum - 1]['J'][t]}: {dist} | Costo de transporte: {1.25 * dist} | Emisiones: {1.5 * dist}")
                                t += 1

                            k += 1

                            print("")
                        break                   
            continue
        continue


    return 0


if __name__ == "__main__":
    main()