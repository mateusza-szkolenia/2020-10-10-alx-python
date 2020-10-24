x = 123

print("Nowoczesna metoda uzywajaca f-stringow")
print( f"x={x}#" )       # po prostu napisz liczbe
print( f"x={x:10}#" )    # wyrownaj do prawej do 10 cyfr
print( f"x={x:2}#" )     # wyrownaj do prawej do 2 cyfr, ale nie zadziala, bo liczba ma 3 cyfry
print( f"x={x:<10}#")    # wyrownaj do lewej do 10 cyfr

# Metoda używająca składni printf() z języka C
print("Metoda uzywajaca %d:")
print( "x=%d" % (x) )
print( "x=%10d" % (x) )
print( "x=%2d" % (x) )
print( "x=%-10d" % (x) )

# Uzycie tabulatora
print( "liczby:\t1\t2\t3")
print( f"x=\t{x}" )

# Brak przejscia do nowej linii:
print("Mateusz ", end="")
print("A. ", end="")
print("A", end="" )
print("LX") # dopieru tu bedzie enter
