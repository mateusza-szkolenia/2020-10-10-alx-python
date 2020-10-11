x = int(input("Podaj X:"))
y = int(input("Podaj Y:"))

if 0 <= x <= 100 and 0 <= y <= 100:
    if x <= 10:
        if y <= 10:
            print("Gracz znajduje się w lewym dolnym rogu")
        elif y >= 90:
            print("Gracz znajduje się w lewym górnym rogu")
        else:
            print("Gracz znajduje się przy lewej krawędzi")
    elif x >= 90:
        if y <= 10:
            print("Gracz znajduje się w prawym dolnym rogu")
        elif y >= 90:
            print("Gracz znajduje się w prawym górnym rogu")
        else:
            print("Gracz znajduje się przy prawej krawędzi")
    else:
        if y <= 10:
            print("Gracz znajduje się przy dolnej krawędzi")
        elif y >= 90:
            print("Gracz znajduje się przy górnej")
        else:
            print("Gracz znajduje się na środku")
else:
    print("Poza planszą")