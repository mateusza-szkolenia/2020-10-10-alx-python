# Napisz funkcje sprawdzajaca, czy dana liczba jest liczba pierwsza.
# Przykład uzycia:
# >>> czy_jest_pierwsza(10)
# False
# >>> czy_jest_pierwsza(17)
# True

def czy_jest_pierwsza( n ):
    for i in range( 2, n ):
        if i**2 > n:
            break
        reszta = n % i
        #print(f"{n:3} / {i:3}  {n/i}  ==> {reszta:3}")
        if reszta == 0:
            # na pewno nie jest liczba pierwsza
            return False
        else:
            # sprawdzamy dalej...
            # return True # ZLE!!!!
            pass
    return True

p = czy_jest_pierwsza( 942841 )
print(p)
