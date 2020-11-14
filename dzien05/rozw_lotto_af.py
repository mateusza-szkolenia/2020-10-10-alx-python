import random

win = []
los = []
trafione6 = 0
trafione5 = 0
trafione4 = 0
trafione3 = 0

for a in range(6):
    win.append(str(random.randint(1, 49)))

x = set(win)

for b in range(6 * 100000):
    while True:
        liczba = str(random.randint(1, 49))
        if liczba in los:
            pass
        else:
            los.append(liczba)
            break
    if len(los) == 6:
        y = set(los)
        z = x&y
        if len(z) == 6:
            trafione6 += 1
        if len(z) == 5:
            trafione5 += 1
        if len(z) == 4:
            trafione4 += 1
        if len(z) == 3:
            trafione3 += 1
        los.clear()


print(x)
print(trafione6)
print(trafione5)
print(trafione4)
print(trafione3)