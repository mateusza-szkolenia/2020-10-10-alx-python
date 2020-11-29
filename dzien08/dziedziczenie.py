class Czlowiek:
    def __init__(self, imie, nazwisko ):
        self._imie = imie
        self._nazwisko = nazwisko

    @property
    def imie_i_nazwisko(self):
        return f"{self._imie} {self._nazwisko}"

    def przedstaw_sie(self):
        print(f"Jestem {self.kim_jestem} o imieniu {self.imie_i_nazwisko}")
    kim_jestem = "czlowiekiem"

class Pracownik(Czlowiek):
    def pracuj(self):
        print(f"Pracuje... (powiedzial {self.imie_i_nazwisko})")
    kim_jestem = "pracownikiem"

class Menedzer(Pracownik):
    def dodaj_pracownika(self, pracownik ):
        if type(pracownik) != Pracownik:
            print(f"Nie mozna dodac {pracownik} jako pracownika")
            return
        self._pracownicy.append( pracownik )
    def przedstaw_pracownikow(self):
        for p in self._pracownicy:
            p.przedstaw_sie()
    def przedstaw_sie(self):
        print("Oto moj zespol:")
        self.przedstaw_pracownikow()
        print("---KONIEC---")

    kim_jestem = "menedzerem"
    _pracownicy = []

m = Menedzer("Piotr", "S")
p1 = Pracownik("Zygfryd", "Z")
p2 = Pracownik("Zygmunt", "N")
c1 = Czlowiek("Jan","X")
c2 = Czlowiek("Roman", "Z")

m.dodaj_pracownika( p1 )
m.dodaj_pracownika( p2 )
#m.dodaj_pracownika( c1 )

ludzie = [ m, p1, p2, c1, c2 ]

#for ktos in ludzie:
#    ktos.przedstaw_sie()
#    if type(ktos) == Pracownik:
#        ktos.pracuj()

#m.przedstaw_sie()

# to jest klasa <class '__main__.Czlowiek'>
print( Czlowiek )

# to jest obiekt klasy Czlowiek <__main__.Czlowiek object at 0x00000000021E6308>
print( c1 )

# to rowniez jest klasa Czlowiek (jak wyzej) <class '__main__.Czlowiek'>
print( type(c1) )

# to jest metoda konkretnego obiektu
print( c1.przedstaw_sie )

# to jest po prostu funkcja, oderwana od jakiegokolwiek obiektu
print( Czlowiek.przedstaw_sie )


