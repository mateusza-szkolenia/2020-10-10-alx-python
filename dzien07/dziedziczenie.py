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
        self._pracownicy.append( pracownik )
    def przedstaw_pracownikow(self):
        for p in self._pracownicy:
            p.przedstaw_sie()
    kim_jestem = "menedzerem"
    _pracownicy = []

m = Menedzer("Piotr", "S")
p1 = Pracownik("Zygfryd", "Z")
p2 = Pracownik("Zygmunt", "N")
c1 = Czlowiek("Jan","X")
c2 = Czlowiek("Roman", "Z")

m.dodaj_pracownika( p1 )
m.dodaj_pracownika( p2 )

ludzie = [ m, p1, p2, c1, c2 ]

#for ktos in ludzie:
#    ktos.przedstaw_sie()
#    if type(ktos) == Pracownik:
#        ktos.pracuj()

m.przedstaw_pracownikow()
