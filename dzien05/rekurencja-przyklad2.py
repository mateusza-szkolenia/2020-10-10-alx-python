xxx = [ 45, 67, [ 12, 12, [ 344, 34], 11, 11 ], 8, [ 23, 34 ] ]

def len_r(lista):
    dlugosc = 0
    for element in lista:
        #print( f"- {element}" )
        if type(element) == int:
            dlugosc += 1
        elif type(element) == list:
            dlugosc += len_r(element)
    return dlugosc

print(len_r(xxx))