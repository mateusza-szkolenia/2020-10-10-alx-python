import Miernictwo

p1 = Miernictwo.Pole( 60000, 'ha' )
p2 = Miernictwo.Pole( 1, 'km2' )

#print( p1 + p2 )

d1 = Miernictwo.Dlugosc( 13, 'mi')
d2 = Miernictwo.Dlugosc( 2500, 'm')

#print( d2.konwertuj_na('km') )
print( p1 / d1 )
