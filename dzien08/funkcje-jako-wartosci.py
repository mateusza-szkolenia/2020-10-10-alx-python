def abc(a, b):
    return a+b


x = abc
rozne_funkcje = [ print, abc ]

print( abc )
print( print )
print( x )
print( x(56,12) )
print( rozne_funkcje )
print( rozne_funkcje[1](4,100) )
