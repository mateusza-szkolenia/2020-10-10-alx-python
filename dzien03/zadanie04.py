poczatek = 0
koniec = 100

ile = 0

for i in range( poczatek, koniec + 1 ):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile += 1

print(f"W przedziale [{poczatek}, {koniec}] liczb podzielnych przez 3 albo 5 jest: {ile}")