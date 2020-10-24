# nie sa mniejsze od 100
# po podniesieniu do 13 potegi daja reszte z dzielenia przez 7 rozna od 2
# po podzieleniu przez 3 daja reszte inna niz 1

zb1 = set()
zb2 = set()

for i in range( 1000 ):
    if i < 100:
        continue
    if (i**13) % 7 == 2:
        continue
    if ( i % 3 ) == 1:
        continue
    print( i )
    zb1 |= { i }

# sposob 1:
for i in range( 1000 ):
    if i >= 100 and (i**13) % 7 != 2 and (i%3) != 1:
        print( i )
        zb2 |= { i }

print( zb1 == zb2 )
