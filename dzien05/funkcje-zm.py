def lista_osob2( osoby ):
    for o in osoby:
        print(f"* {o}")

def lista_osob( *args, **kwargs ):
    for o in args:
        print(f"* {o}")
    print(f"{kwargs}")

lista_osob( "Mateusz", "Maciej", "Tomasz", tytul="Pan", firma ="ALX" )
lista_osob2( ["Mateusz", "Maciej", "Tomasz"] )
lista_osob2( ("Mateusz", "Maciej", "Tomasz" ) )
