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
        print(f"Pracuje w firmie: {self._firma._nazwa}, zarabiam: {self._wynagrodzenie}, moj szef to: {self._szef.imie_i_nazwisko if self._szef != None else '---' }")
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

f = Firma("ABCXYZ")
m = Menedzer("Piotr", "S")

f.ustaw_szefa( m )
m.dodaj_pracownika( Pracownik("Zygfryd", "Z") )
m.dodaj_pracownika( Pracownik("Zygmunt", "N") )
m.dodaj_pracownika( Pracownik("Alfred", "Z") )
m.dodaj_pracownika( Pracownik("Benedykt", "Z") )
m.dodaj_pracownika( Pracownik("Cezary", "Z") )
m.usun_pracownika( m._pracownicy[0] )
m.usun_pracownika( m._pracownicy[1] )
m.usun_pracownika( m._pracownicy[1] )

m.ustal_wynagrodzenie(9000)
m.ustaw_wynagrodzenie_zespolu(4000)

#f.przedstaw_firme()

p = Pracownik("Xawery","ABC")

del m
del f

print(Czlowiek._licznik)

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

