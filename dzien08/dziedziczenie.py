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

    @property
    def imie_i_nazwisko(self):
        return f"{self._imie} {self._nazwisko}"

    def przedstaw_sie(self):
        print(f"Jestem {self.kim_jestem} o imieniu {self.imie_i_nazwisko}")
    kim_jestem = "czlowiekiem"

class Pracownik(Czlowiek):
    def pracuj(self):
        print(f"Pracuje... (powiedzial {self.imie_i_nazwisko})")
    def ustal_wynagrodzenie(self, wynagrodzenie):
        self._wynagrodzenie = wynagrodzenie
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Pracuje w firmie: {self._firma._nazwa}, zarabiam: {self._wynagrodzenie}, moj szef to: {self._szef.imie_i_nazwisko if self._szef != None else '---' }")
    @property
    def koszt_calkowity(self):
        return 2000 + self._wynagrodzenie * 1.5
    def ustaw_firme(self, firma ):
        self._firma = firma
    def ustaw_szefa(self, szef):
        if type(szef) == Menedzer:
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

f = Firma("ABCXYZ")
m = Menedzer("Piotr", "S")
p1 = Pracownik("Zygfryd", "Z")
p2 = Pracownik("Zygmunt", "N")
c1 = Czlowiek("Jan","X")
c2 = Czlowiek("Roman", "Z")

f.ustaw_szefa(m)
m.dodaj_pracownika( p1 )
m.dodaj_pracownika( p2 )


m.ustal_wynagrodzenie(9000)
m.ustaw_wynagrodzenie_zespolu(4000)

f.przedstaw_firme()


# to jest klasa <class '__main__.Czlowiek'>
#print( Czlowiek )

# to jest obiekt klasy Czlowiek <__main__.Czlowiek object at 0x00000000021E6308>
#print( c1 )

# to rowniez jest klasa Czlowiek (jak wyzej) <class '__main__.Czlowiek'>
#print( type(c1) )

# to jest metoda konkretnego obiektu
#print( c1.przedstaw_sie )

# to jest po prostu funkcja, oderwana od jakiegokolwiek obiektu
#print( Czlowiek.przedstaw_sie )

