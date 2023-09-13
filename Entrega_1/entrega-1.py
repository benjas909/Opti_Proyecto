import random as r

INSTANCES_S = []
INSTANCES_M = []
INSTANCES_L = []

def generate_s(it):
    I = []
    J = []
    match it:
        case 1:
            
            for _ in range(r.randint(5, 7)):
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
            
            for _ in range(r.randint(6, 10)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 2:
            
            for _ in range(r.randint(8, 12)):
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
            
            for _ in range(r.randint(10, 20)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 3:
        
            for _ in range(r.randint(13, 18)):
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
            
            for _ in range(r.randint(20, 30)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

        case 4:
            
            for _ in range(r.randint(19, 23)):
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
            
            for _ in range(r.randint(30, 40)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue
        
        case 5:
            
            for _ in range(r.randint(24, 30)):
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
            
            for _ in range(r.randint(40, 50)):
                while True:

                    point = (r.randint(-75, 75), r.randint(-75, 75))

                    if point not in J:
                        J.append(point)
                        break

                    continue

    instances = {"I": I, "J": J}

    return instances
    

def generate_m(it):
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


def generate_l(it):
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


def main():

    for i in range(1, 6):
        INSTANCES_S.append(generate_s(i))
        INSTANCES_M.append(generate_m(i))
        INSTANCES_L.append(generate_l(i))

    for i in range(3):
        if i == 0:
            print("Instancias pequeñas:")
            for j in range(5):
                print(f"Instancia {j + 1}:")
                k = 0
                while (k < len(INSTANCES_S[j]["J"])): 
                    if (k < len(INSTANCES_S[j]["I"])):
                        print(f" I: {INSTANCES_S[j]['I'][k]}, J: {INSTANCES_S[j]['J'][k]}")
                    else:
                        print(f"                 J: {INSTANCES_S[j]['J'][k]}")    
                    
                    k += 1

        elif i == 1:
            print("Instancias medianas:")
            for j in range(5):
                print(f"Instancia {j + 1}:")
                k = 0
                while (k < len(INSTANCES_M[j]["J"])): 
                    if (k < len(INSTANCES_M[j]["I"])):
                        print(f" I: {INSTANCES_M[j]['I'][k]}, J: {INSTANCES_M[j]['J'][k]}")
                    else:
                        print(f"                 J: {INSTANCES_M[j]['J'][k]}")    
                    
                    k += 1
            
        elif i == 2:
            print("Instancias grandes:")
            for j in range(5):
                print(f"Instancia {j + 1}:")
                k = 0
                while (k < len(INSTANCES_L[j]["J"])): 
                    if (k < len(INSTANCES_L[j]["I"])):
                        print(f" I: {INSTANCES_L[j]['I'][k]}, J: {INSTANCES_L[j]['J'][k]}")
                    else:
                        print(f"                 J: {INSTANCES_L[j]['J'][k]}")   
                    
                    k += 1

    return 0


if __name__ == "__main__":
    main()