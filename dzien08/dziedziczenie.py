import random

class Firma:
    def __init__(self, nazwa ):
        self._nazwa = nazwa
    def przedstaw_firme(self):
        print(f"Oto firma {self._nazwa}")
        print(f"Szefem jest:")
        self._szef.przedstaw_sie()
    def ustaw_szefa(self, szef):
        if type(szef) == Menedzer:
            self._szef = szef
            szef.ustaw_firme( self )
    _szef = None

class Czlowiek:
    def __init__(self, imie, nazwisko ):
        self._imie = imie
        self._nazwisko = nazwisko
        #self._licznik = random.randint(100,200)
        Czlowiek._licznik += 1
    def __del__(self):
        print("Zegnajcie")
    @property
    def imie_i_nazwisko(self):
        return f"{self._imie} {self._nazwisko}"

    def przedstaw_sie(self):
        print(f"Jestem {self.kim_jestem} o imieniu {self.imie_i_nazwisko}")
    kim_jestem = "czlowiekiem"
    _licznik = 0

class Pracownik(Czlowiek):

    def pracuj(self):
        print(f"Pracuje... (powiedzial {self.imie_i_nazwisko})")
    def ustal_wynagrodzenie(self, wynagrodzenie):
        self._wynagrodzenie = wynagrodzenie
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Pracuje w firmie: {self._firma._nazwa if self._firma != None else '---'}, zarabiam: {self._wynagrodzenie}, moj szef to: {self._szef.imie_i_nazwisko if self._szef != None else '---' }")
    @property
    def koszt_calkowity(self):
        return 2000 + self._wynagrodzenie * 1.5
    def ustaw_firme(self, firma ):
        self._firma = firma
    def ustaw_szefa(self, szef):
        if type(szef) == Menedzer or szef == None:
            self._szef = szef
    kim_jestem = "pracownikiem"
    _wynagrodzenie = 0
    _firma = None
    _szef = None

class Menedzer(Pracownik):
    def dodaj_pracownika(self, pracownik ):
        if type(pracownik) != Pracownik:
            print(f"Nie mozna dodac {pracownik} jako pracownika")
            return
        pracownik.ustaw_firme(self._firma)
        pracownik.ustaw_szefa(self)
        self._pracownicy.append( pracownik )
    def usun_pracownika(self, pracownik ):
        pracownik.ustaw_firme( None )
        pracownik.ustaw_szefa( None )
        self._pracownicy.remove( pracownik )

    def przedstaw_pracownikow(self):
        for p in self._pracownicy:
            p.przedstaw_sie()
    def przedstaw_sie(self):
        super().przedstaw_sie()
        #Czlowiek.przedstaw_sie(self)
        print(f"Oto moj zespol w firmie {self._firma._nazwa}:")
        self.przedstaw_pracownikow()
        print("---KONIEC---")
    def ustaw_wynagrodzenie_zespolu(self, wynagrodzenie):
        for p in self._pracownicy:
            p.ustal_wynagrodzenie( wynagrodzenie )
    @property
    def koszt_calkowity(self):
        return super().koszt_calkowity + sum([ p.koszt_calkowity for p in self._pracownicy ]) + self._budzet_integracyjny

    kim_jestem = "menedzerem"
    _pracownicy = []
    _budzet_integracyjny = 3000

def wyn( prac ):
    return prac._wynagrodzenie
def imie( prac ):
    return len(prac._imie)

p1 = Pracownik("Alicja", "XXX")
p1.ustal_wynagrodzenie(4000)
p2 = Pracownik("Basia", "K")
p2.ustal_wynagrodzenie(3500)
p3 = Pracownik("Katarzyna", "Z")
p3.ustal_wynagrodzenie(9000)
p4 = Pracownik("Celina", "A")
p4.ustal_wynagrodzenie(4100)

pracownice = [p1,p2,p3,p4]

def funkcja_pomocnicza( prac ):
    return ( len(prac._nazwisko), prac._nazwisko)

# bez uzycia lambdy:
# pracownice.sort(key=funkcja_pomocnicza)

# z uzyciem lambdy, ale w zmiennej
funkcja_pomocnicza2 = lambda prac : ( len(prac._nazwisko), prac._nazwisko)
pracownice.sort(key=funkcja_pomocnicza2)

pracownice.sort(key=lambda prac : ( len(prac._nazwisko), prac._nazwisko)  )

for p in pracownice:
    p.przedstaw_sie()

