import random

def losuj():
    wynik = set()
    while len(wynik) < 6:
        wynik = wynik | set([random.randint(1,49)])
    return wynik
def ile_trafien(a,b):
    return len(a&b)

wygrane = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
prawdopodobienstwa = {
    6 : 1 / 13_983_816,
    5 : 1 / 54_201,
    4 : 1 / 1_032,
    3 : 1 / 57,
    2 : 13.2 / 100,
    1 : 41.3 / 100,
    0 : 43.6 / 100
}
losowanie_lotto = losuj()
n = int(input("Podaj liczbę zakładów do symulowania: "))
for i in range(n+1):
    kupon = losuj()
    trafienia = ile_trafien(losowanie_lotto, kupon)
    wygrane[trafienia] += 1
# print(wygrane)
for traf, ilosc_trafien in wygrane.items():
    print(f"Wygranych: {traf} było: {ilosc_trafien:>7}. Wyliczone prawdopobienstwo na próbie {n}: {ilosc_trafien/n*100:7.2f}, Wikipedia: {prawdopodobienstwa[traf]*100:.2f}")


