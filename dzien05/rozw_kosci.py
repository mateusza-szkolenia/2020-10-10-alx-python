#     1: XX   (2)
#     2: XX   (2)
#     3: XXX  (3)
#     4:      (0)
#     5: X    (1)
#     6: XX   (2)
# [ ( 1, 2 ), (2,2), (3,3), (4,0) ]

import random

def rzut():
    return random.randint(1,6)

def wykres( dane ):
    SZER = 50
    najwieksza = max([ wartosc for (klucz, wartosc) in dane ])
    for klucz, wartosc in dane:
        #print( wartosc / najwieksza )
        #print( f"{klucz} {'X' * wartosc :10}")
        print(f"{klucz:5}: {('X' * int( wartosc/najwieksza * SZER) ):{SZER}} ({wartosc})")

ILE_RZUTOW = 1000

rzuty = [ rzut() for i in range( ILE_RZUTOW ) ]
print(rzuty)

wyniki = [0,0,0,0,0,0,0]

for wynik in range(1,7):
    wyniki[wynik] = len( [ None for r in rzuty if r == wynik ] )

print(wyniki)

wykres( list(enumerate(wyniki)) )