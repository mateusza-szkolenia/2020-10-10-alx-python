uczniowie = [
  { "imie" : "Helena", "nazwisko" : "C.", "oceny" : "2 2 4 4 2 3 1 4" },
  { "imie" : "Artur", "nazwisko" : "U.", "oceny" : "4 3 5 6 3 4 6 3" },
  { "imie" : "Julian", "nazwisko" : "L.", "oceny" : "3 3 4 3 4 3 4 3" },
  { "imie" : "Gerturda", "nazwisko" : "H.", "oceny" : "4 5 3 3 3 2 4 4" },
  { "imie" : "Artur", "nazwisko" : "L.", "oceny" : "4 1 5 5 5 2 2 1" },
  { "imie" : "Artur", "nazwisko" : "L.", "oceny" : "3 6 5 4 3 6 3 5" },
  { "imie" : "Gerturda", "nazwisko" : "O.", "oceny" : "6 6 5 3 3 4 3 4" },
  { "imie" : "Julian", "nazwisko" : "L.", "oceny" : "6 1 6 4 1 1 5 1" },
  { "imie" : "Julian", "nazwisko" : "O.", "oceny" : "1 4 5 1 3 3 4 5" },
  { "imie" : "Artur", "nazwisko" : "M.", "oceny" : "3 3 5 4 4 4 4 4" },
  { "imie" : "Tomasz", "nazwisko" : "A.", "oceny" : "5 4 1 4 1 5 2 2" },
  { "imie" : "Justyna", "nazwisko" : "H.", "oceny" : "5 3 3 4 2 2 2 5" },
  { "imie" : "Justyna", "nazwisko" : "B.", "oceny" : "1 2 1 2 5 5 1 1" },
  { "imie" : "Gerturda", "nazwisko" : "W.", "oceny" : "5 2 4 1 4 4 5 4" },
  { "imie" : "Damian", "nazwisko" : "I.", "oceny" : "2 3 2 2 1 1 3 1" },
  { "imie" : "Jacek", "nazwisko" : "I.", "oceny" : "4 4 3 3 3 4 4 4" }
]

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

for u in uczniowie:
    print( formatuj( '$imie $nazwisko [$oceny]', **u ) )