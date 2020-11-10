#W tabliczce mnożenia zastąpić wartości specjalnymi znakami

print(f"\t", end="")
for kolumna in range(10):
    print(f"\t{kolumna:<3}", end="")
print()

for wiersz in range(10):
    print(f"\t{wiersz}:", end="")
    for kolumna in range(10):
        wynik = wiersz * kolumna
        if wynik <= 5:
            iks = "."
            print(f"\t{iks:<3}", end ="")
        elif 6 <= wynik <= 10:
            iks = "o"
            print(f"\t{iks:<3}", end="")
        elif 11 <= wynik <= 15:
            iks = "0"
            print(f"\t{iks:<3}", end="")
        elif 16 <= wynik <= 20:
            iks = "0"
            print(f"\t{iks:<3}", end="")
        else:
            print(f"\t@", end="")
    print()