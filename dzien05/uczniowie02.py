uczniowie = [
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
        print(f"Utworzono nowego ucznia o imieniu {imie}!")
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = [int(o) for o in oceny.split()]
    def przywitaj_sie(self):
        print(f"Dzien dobry po raz {self.licznik}, jestem uczniem i nazywam sie {self.imie}!")
        self.licznik += 1
    def srednia(self):
        return sum(self.oceny) / len(self.oceny)
    def czy_klasyfikowany(self):
        return len([o for o in self.oceny if o == 1]) <= 1
    licznik = 1

u1 = Uczen("Maksymilian", "X.", "1 2 3 4 5 6")
u2 = Uczen("Andrzej", "Z.", "5 5 5 6 6 6")
u3 = Uczen("Zenon", "X", "1 1 3 1 4 1")
print(f"U1 ma średnią {u1.srednia()}")
print(f"U3 klasyfikowany: {u3.czy_klasyfikowany()}")
u1.przywitaj_sie()
u2.przywitaj_sie()
u1.przywitaj_sie()
u1.przywitaj_sie()
u2.przywitaj_sie()



def opisz_ucznia( uczen ):
    return f"{uczen['imie']:12} {uczen['nazwisko']:4} {srednia_ucznia(uczen):6.2f} {czy_klasyfikowany(uczen):3} {czy_czerwony_pasek(uczen):3}"



def czy_czerwony_pasek( uczen ):
    return srednia_ucznia(uczen) >= 4.75 and czy_klasyfikowany(uczen)

#for u in uczniowie:
#    print(opisz_ucznia(u))
