#     1: XX   (2)
#     2: XX   (2)
#     3: XXX  (3)
#     4:      (0)
#     5: X    (1)
#     6: XX   (2)
# [ (1,2), (2,2), (3,3), (4,0), (5,1), (6,2)]
# 10 rzutow
import random
def rzut():
    return random.randint(1,6)

def wykres( dane ):
    SZER = 50
    najwieksza = max([ wartosc for (klucz, wartosc) in dane ])
    for klucz, wartosc in dane:
        # print( wartosc / najwieksza )
        # print( f"{klucz} {'X' * wartosc :10}")
        # print(f"{klucz:5}: {('X' * wartosc ):50} ({wartosc})")
        print(f"{klucz:5}: {('X' * int( wartosc/najwieksza * SZER) ):{SZER}} ({wartosc})")

ilosc_rzutow = 10

rzuty = [rzut() for i in range(ilosc_rzutow)]
print(rzuty)
tablica_wynikow = [0,0,0,0,0,0,0]

for oczka in [1,2,3,4,5,6]:
    tablica_wynikow[oczka] = len([ r for r in rzuty if r == oczka])

wykres(list(enumerate(tablica_wynikow)))