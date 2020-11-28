class Czlowiek:
    def __init__(self, imie, nazwisko ):
        self._imie = imie
        self._nazwisko = nazwisko
    def przedstaw_sie(self):
        print(f"Jestem {self.kim_jestem} o imieniu {self._imie} {self._nazwisko}")
    kim_jestem = "czlowiekiem"

class Pracownik(Czlowiek):
    def pracuj(self):
        print(f"Pracuje... (powiedzial {self._imie})")
    kim_jestem = "pracownikiem"

ludzie = [
    Pracownik("Zygfryd", "Z"),
    Czlowiek("Jan","X"),
    Czlowiek("Roman", "Z")
]

for ktos in ludzie:
    ktos.przedstaw_sie()
    if type(ktos) == Pracownik:
        ktos.pracuj()