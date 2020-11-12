# W tabliczce mnożenia zastąpić liczby podzielne przez 2, 3 lub 5 sekwencją iksów o długości odpowiadającej długości wyniku.
print(f"\t", end="")
for kolumna in range(10):
    print(f"\t{kolumna:<3}", end="")
print()

for wiersz in range(10):
    print(f"\t{wiersz}:", end="")
    for kolumna in range(10):
        wynik = wiersz * kolumna
        if wynik % 5 == 0 or wynik % 3 == 0 or wynik % 2 == 0:
            iksy = len(str(wynik))*"x"
            print(f"\t{iksy:<3}", end ="")
        else:
            print(f"\t{wynik:<3}", end="")

    print()

