import random as r

INSTANCES_P = []
INSTANCES_M = []
INSTANCES_G = []

def generate_s(it):
    I = []
    J = []
    match it:
        case 1:
            
            for _ in range(r.randint(5, 7)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(6, 10)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 2:
            
            for _ in range(r.randint(8, 12)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(10, 20)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 3:
        
            for _ in range(r.randint(13, 18)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(20, 30)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

        case 4:
            
            for _ in range(r.randint(19, 23)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(30, 40)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 5:
            
            for _ in range(r.randint(24, 30)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(40, 50)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

    instances = {"I": I, "J": J}

    return instances
    

def generate_m(it):
    I = []
    J = []
    match it:
        case 1:

            for _ in range(r.randint(32, 38)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(50, 65)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 2:
            
            for _ in range(r.randint(39, 45)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(65, 80)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 3:
        
            for _ in range(r.randint(46, 53)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(80, 95)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

        case 4:

            for _ in range(r.randint(54, 65)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(95, 110)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 5:

            for _ in range(r.randint(66, 72)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(110, 125)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

    instances = {"I": I, "J": J}

    return instances


def generate_g(it):
    I = []
    J = []
    match it:
        case 1:
            
            for _ in range(r.randint(72, 81)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(125, 145)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 2:
            
            for _ in range(r.randint(82, 91)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(145, 165)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 3:
        
            for _ in range(r.randint(92, 101)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(165, 185)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

        case 4:

            for _ in range(r.randint(102, 111)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(185, 205)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))
        
        case 5:

            for _ in range(r.randint(112, 131)):
                x = r.randint(-300, 300)
                if (abs(x) > 75):
                    y = r.randint(-300, 300)
                else:
                    y = r.randint(*r.choice([(-300, -76),(76, 300)]))
                
                I.append((x, y))
            
            for _ in range(r.randint(205, 225)):
                J.append((r.randint(-75, 75), r.randint(-75, 75)))

    instances = {"I": I, "J": J}

    return instances


def main():

    for i in range(1, 6):
        INSTANCES_P.append(generate_s(i))
        INSTANCES_M.append(generate_m(i))
        INSTANCES_G.append(generate_g(i))

    for i in range(3):
        if i == 0:
            print("Instancias pequeñas:")
            for j in range(5):
                print(f"Instancia {j + 1}:")
                k = 0
                while (k < len(INSTANCES_P[j]["J"])): 
                    if (k < len(INSTANCES_P[j]["I"])):
                        print(f" I: {INSTANCES_P[j]['I'][k]}, J: {INSTANCES_P[j]['J'][k]}")
                    else:
                        print(f"                 J: {INSTANCES_P[j]['J'][k]}")    
                    
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
                while (k < len(INSTANCES_G[j]["J"])): 
                    if (k < len(INSTANCES_G[j]["I"])):
                        print(f" I: {INSTANCES_G[j]['I'][k]}, J: {INSTANCES_G[j]['J'][k]}")
                    else:
                        print(f"                 J: {INSTANCES_G[j]['J'][k]}")   
                    
                    k += 1

    return 0


if __name__ == "__main__":
    main()