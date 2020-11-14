# Zaimplementuj funkcje formatujaca podane napisy.
# Przykład uzycia:
# >>> formatuj(
#    'koszt $cena PLN',
#    'kwota $cena brutto',
#    cena=10,
#    )
#
# wynik: 'koszt 10 PLN\nkwota 10 brutto'

def formatuj( *args, **kwargs ):
    wynik = ""
    for napis in args:
        #print(f"{napis}")
        for klucz, wartosc in kwargs.items():
            #print(f"-- {klucz} = {wartosc}")
            napis = napis.replace( "$" + klucz, wartosc )
            #print(f"Po zmianie: {napis}")
        wynik = wynik + napis + "\n"
    return wynik

x = formatuj(
    "Nazywam sie $imie i pracuje w $firma",
    "$firma miesci sie w miescie $miasto",
    imie="Mateusz",
    miasto="Warszawa",
    firma="ALX"
)

print(x)

# wynik ma byc: "Nazywam sie Mateusz i pracuje w ALX\nALX miesci sie w miescie Warszawa"