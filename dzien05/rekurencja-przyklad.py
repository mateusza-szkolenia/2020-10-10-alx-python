xxx = [ 45, 67, [ 12, 12, [ 344, 34], 11, 11 ], 8, [ 23, 34 ] ]

def suma_r( lista ):
    suma = 0
    for element in lista:
        #print( f"- {element}" )
        if type(element) == int:
            suma += element
        elif type(element) == list:
            suma += suma_r( element )
    return suma

print( suma_r( xxx ) )