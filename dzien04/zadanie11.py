# Napisz program zliczajacy liczbe unikalnych liczb wprowadzonych
# przez uzytkownika. Sprawdz jak duzo z tych liczb jest liczbami
# parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
# iloczynu.

#liczby = [ 10, 20, 10, 30, 13, 13, 30, 10, 20, 11, 10, 777, 800 ]
liczby = []

while True:
    x = input( "Podaj liczbe lub napisz KONIEC: " ).upper()
    if x == "KONIEC":
        break
    liczby.append( int(x) )

print(f"Liczby: {liczby}")
print(f"Liczba liczb: {len(liczby)} ")

bez_powt = set( liczby )
print(f"Liczby unikalne: {bez_powt}")

bez_powt2 = list(set( liczby ))
print(f"Liczby unikalne: {bez_powt2}")

liczby_parzyste = set( range(0, 100+1, 2) )
liczbyx = liczby_parzyste & bez_powt

print(f"Liczby X: {liczbyx}")

