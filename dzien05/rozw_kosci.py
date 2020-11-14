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
    for klucz, wartosc in dane:
        #print( f"{klucz} {'X' * wartosc :10}")
        print(f"{klucz:5}: {('X' * wartosc ):50} ({wartosc})")

rzuty = [ rzut() for i in range(100) ]
print(rzuty)

wyniki = [0,0,0,0,0,0,0]

for wynik in [1,2,3,4,5,6]:
    wyniki[wynik] = len( [ r for r in rzuty if r == wynik ] )

wykres( enumerate(wyniki) )