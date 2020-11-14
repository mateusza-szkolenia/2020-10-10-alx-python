# Zadanie #6
# Zaimplementuj funkcje spłaszczajaca podana liste.
# Przykład uzycia:
# >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
# [1, 2, 3, 4, 5, 6, 7]

xxx = [ 45, 67, [ "sss", 12, [ "x", 34], False, 11 ], 8, [ 23, 34 ] ]

def splaszcz(lista):
    wynik = []
    for element in lista:
        if type(element) != list:
            wynik += [ element ]
        elif type(element) == list:
            wynik += splaszcz(element)
    return wynik

print(splaszcz(xxx))