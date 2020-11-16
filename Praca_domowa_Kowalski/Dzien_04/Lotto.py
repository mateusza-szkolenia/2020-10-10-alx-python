import random

def losowanie():
    los = set()
    while len(los) < 6:
        los = los | set( [random.randint(1, 49)])
    return los

def ilosc_trafien(a, b):
    return len(a & b)

wygrane = {6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
prawdopodobienstwa = {
    6 : 1 / 13_983_816,
    5 : 1 / 54_201,
    4 : 1 / 1_032,
    3 : 1 / 57,
    2 : 13.2 / 100,
    1 : 41.3 / 100,
    0 : 43.6 / 100
}

kombinacja_lotto = losowanie()
N = 1000
for n in range(N):
    los = losowanie()
    liczba_trafien = ilosc_trafien(kombinacja_lotto, los)
    wygrane[liczba_trafien] += 1

print(wygrane)
for wygrane, l_trafien in wygrane.items():
    print(f"Trafienie {wygrane} cyfr: {l_trafien:5} razy. Prawdopodobieństwo: {l_trafien/N*100:6.2f}   Wikipedia: {prawdopodobienstwa[wygrane]*100:6.2f} ")
