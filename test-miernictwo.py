import Miernictwo

p1 = Miernictwo.Pole( 45, 'km2' )
p2 = Miernictwo.Pole( 30, 'mi2' )

d1 = Miernictwo.Dlugosc( 2, 'km')
d2 = Miernictwo.Dlugosc( 2500, 'm')

print( d2.konwertuj_na('km') )
print( d1 * d2 )
