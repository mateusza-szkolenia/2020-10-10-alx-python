# Mając daną listę liczb, znaleźć najmniejszą i największą z nich

liczby = [ 999, 100, 101, 999, 999, 200, 80, 10, 60 ]

najmniejsza = None
najwieksza = None
poz_najmniejsza = None
poz_najwieksza = None

for p, biezaca in enumerate( liczby ):
    if najmniejsza == None or biezaca <= najmniejsza:
        najmniejsza = biezaca
        poz_najmniejsza = p
    if najwieksza == None or biezaca >= najwieksza:
        najwieksza = biezaca
        poz_najwieksza = p

print( f"Najmniejsza liczba to: {najmniejsza} (poz: {poz_najmniejsza})" )
print( f"Najwieksza liczba to: {najwieksza} (poz: {poz_najwieksza})" )

wszystkie_min = []
wszystkie_max = []

for p, biezaca in enumerate(liczby):
    print(f"{biezaca}: ", end="")
    if biezaca == najmniejsza:
        print("MIN ", end="")
        wszystkie_min.append( p )
    if biezaca == najwieksza:
        print("MAX ", end="")
        wszystkie_max.append(p)
    print()

print(f"MAX={najwieksza}  pozycje: {wszystkie_max}  wystapien: {len(wszystkie_max)}")
print(f"MIN={najmniejsza}  pozycje: {wszystkie_min}  wystapien: {len(wszystkie_min)}")

# wypisac jako dwie listy WSZYSTKIE pozycje, na ktorych jest element o wartosci najmniejszej i najwiekszej
# Przyklad
# MAX=999 pozycje: [ 0, 3, 4 ] - wystapien: 3
# MIN=10 pozycje: [ 7 ] - wystapien: 1