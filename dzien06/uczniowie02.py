uczniowie_in = [
  { "imie" : "Dariusz", "nazwisko" : "Y.", "oceny" : "4 4 2 3 2 5 2" },
  { "imie" : "Wiktoria", "nazwisko" : "A.", "oceny" : "5 4 4 3 5 3 4" },
  { "imie" : "Natalia", "nazwisko" : "I.", "oceny" : "4 3 4 3 3 3 4" },
  { "imie" : "Tadeusz", "nazwisko" : "A.", "oceny" : "2 3 4 2 2 2 2" },
  { "imie" : "Piotr", "nazwisko" : "R.", "oceny" : "3 3 5 3 2 5 5" },
  { "imie" : "Natalia", "nazwisko" : "I.", "oceny" : "6 6 6 4 5 4 4" },
  { "imie" : "Piotr", "nazwisko" : "L.", "oceny" : "6 6 1 6 6 6 1 6 6 6 6 6 6" },
  { "imie" : "Wiktoria", "nazwisko" : "U.", "oceny" : "3 5 4 2 2 4 2" },
  { "imie" : "Natalia", "nazwisko" : "D.", "oceny" : "3 1 6 6 6 6 1" },
  { "imie" : "Natalia", "nazwisko" : "S.", "oceny" : "4 5 5 3 3 4 5" },
  { "imie" : "Piotr", "nazwisko" : "U.", "oceny" : "1 3 1 3 3 4 3" },
  { "imie" : "Anna", "nazwisko" : "G.", "oceny" : "1 4 4 1 4 3 3" },
  { "imie" : "Anna", "nazwisko" : "G.", "oceny" : "4 4 4 3 3 3 4" },
  { "imie" : "Jakub", "nazwisko" : "N.", "oceny" : "2 4 4 2 3 4 4" }
]

class Uczen:
    def __init__(self, imie="bezimienny", nazwisko="xxx", oceny="" ):
        self._imie = imie
        self._nazwisko = nazwisko
        if type(oceny) == list:
            self._oceny = oceny
        elif type(oceny) == str:
            self._oceny = [int(o) for o in oceny.split()]
        else:
            self._oceny = []
    def __repr__(self):
        return f"Uczen({repr(self._imie)}, {repr(self._nazwisko)}, {repr(self._oceny)})"
    def __str__(self):
        return self._opisz_ucznia()
    def __gt__(self, other):
        # jest to dyskusyjne, jak należy porównywać uczniów...
        return self._nazwisko > other._nazwisko
    def przywitaj_sie(self):
        print(f"Dzien dobry po raz {self._licznik}, jestem uczniem i nazywam sie {self._imie}!")
        self._licznik += 1
    def srednia(self):
        return sum(self._oceny) / len(self._oceny)
    def czy_klasyfikowany(self):
        return len([o for o in self._oceny if o == 1]) <= 1
    def czy_czerwony_pasek(self):
        return self.srednia() >= 4.75 and self.czy_klasyfikowany()
    def _opisz_ucznia(self):
        return f"{self._imie:12} {self._nazwisko:4} {self.srednia():6.2f} {self.czy_klasyfikowany():3} {self.czy_czerwony_pasek():3}"
    _licznik = 1

# konwersja slowników na obiekty
uczniowie = [ Uczen(**u) for u in uczniowie_in ]

#for u in [ uu for uu in uczniowie if uu.czy_klasyfikowany() ]:
#    print( u )

u1 = uczniowie[0]
u2 = uczniowie[1]
print(repr(u1))
