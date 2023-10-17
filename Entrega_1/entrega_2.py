import subprocess as sub

def main():
    print("            1          |          2          |           3           |")
    print("   |      Pequeñas     |      Medianas       |        Grandes        |")
    print("   |    I    |    J    |    I    |     J     |     I     |     J     |")
    print(" 1 |  5 - 7  |  6 - 10 | 32 - 38 |  50 - 65  |  72 - 81  | 125 - 145 |")
    print(" 2 |  8 - 12 | 10 - 20 | 39 - 45 |  65 - 80  |  82 - 91  | 145 - 165 |")
    print(" 3 | 13 - 18 | 20 - 30 | 46 - 53 |  80 - 95  |  92 - 101 | 165 - 185 |")
    print(" 4 | 19 - 23 | 30 - 40 | 54 - 65 |  95 - 110 | 102 - 111 | 185 - 205 |")
    print(" 5 | 24 - 30 | 40 - 50 | 66 - 72 | 110 - 125 | 112 - 131 | 205 - 225 |")

    output = sub.run(["cmd", "/c", "entrega_1edited.py"], shell=True, input="1\n1", stderr = sub.STDOUT, stdout=sub.PIPE, text = True, check=True)
    # outp = sub.check_output("tests3.py", shell = True, input="1\n2", stderr = sub.STDOUT, text = True)
    print(output.stdout)

    return 0

if __name__ == "__main__":
    main()
