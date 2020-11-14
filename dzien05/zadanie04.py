# Zaimplementuj funkcje formatujaca podane napisy.
# Przykład uzycia:
# >>> formatuj(
#    'koszt $cena PLN',
#    'kwota $cena brutto',
#    cena=10,
#    )
#
# wynik: 'koszt 10 PLN\nkwota 10 brutto'

formatuj(
    "Nazywam sie $imie i pracuje w $firma",
    "$firma miesci sie w miescie $miasto",
    imie="Mateusz",
    miasto="Warszawa",
    firma="ALX"
)

# wynik ma byc: "Nazywam sie Mateusz i pracuje w ALX\nALX miesci sie w miescie Warszawa"