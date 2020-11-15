class Dlugosc:
    def __init__(self, wartosc, jednostka='m'):
        if type(wartosc) == str:
            a, b = (wartosc+" "+jednostka).split()[0:2]
            wartosc, jednostka = float(a), b
        self._wartosc = wartosc
        self._jednostka = jednostka
    def _wartosc_w_m(self):
        return self._wartosc * self._mnozniki[self._jednostka]
    def _wartosc_w_jednostce(self, jednostka):
        return self._wartosc_w_m() / self._mnozniki[jednostka]
    def __lt__(self, other):
        return self._wartosc_w_m() < other._wartosc_w_m()
    def __eq__(self, other):
        return self._wartosc_w_m() == other._wartosc_w_m()
    def __neg__(self):
        return -1 * self
    def __add__(self, other):
        if type(other) == Dlugosc:
            return Dlugosc(
                self._wartosc + (
                    other._wartosc
                    if self._jednostka == other._jednostka
                    else other._wartosc_w_jednostce( self._jednostka )
                ),
                self._jednostka
            )
        elif type(other) in (int,float):
            # mam mieszane uczucia, czy klasa powinna sie tak zachowywac :-)
            return Dlugosc( self._wartosc + other, self._jednostka )
        else:
            return None
    def __truediv__(self, other):
        if type(other) == Dlugosc:
            return self._wartosc_w_m() / other._wartosc_w_m()
        elif type(other) in (int, float):
            return Dlugosc( self._wartosc / other, self._jednostka )
        else:
            return None
    def __sub__(self, other):
        return self + ( - other )
    def __mul__(self, other):
        if type( other ) in ( float, int ):
            return Dlugosc( self._wartosc * other, self._jednostka )
        return None
    def __str__(self):
        return f"{self._wartosc:.1f} {self._jednostka}"
    def __repr__(self):
        return f"Dlugosc({repr(self._wartosc)}, {repr(self._jednostka)})"
    def konwertuj_na(self, jednostka):
        return Dlugosc( self._wartosc_w_jednostce(jednostka), jednostka )
    _mnozniki = { 'm': 1, 'km' : 1000, 'mi' : 1_609.344, 'cm' : 0.01, 'in' : 0.0254, 'mm' : 0.001, 'dm' : 0.1, 'ft' : 0.3048 }
    __rmul__ = __mul__

#d = Dlugosc(1, 'mi')    # 1.609km => 160934 cm
#print( d._wartosc_w_jednostce('cm') )

#d3 = Dlugosc( 50, 'cm' )
#d4 = Dlugosc( 10, 'in' ) # okolo 25 cm

#print( d3 + 123 ) # chcemy żeby wynik miał jednostkę cm

print( ( Dlugosc( 5, 'km' ) / 2 + Dlugosc( 10, 'km' ) * 3 ).konwertuj_na('mi')   )
print( Dlugosc( 4, 'mi' ) / Dlugosc( 6, 'km') )   # wynik to 3 (liczba)

d2 = Dlugosc( 0, 'in') + 3 * Dlugosc( "24.5 cm" ) + Dlugosc( "1 ft" ) / 3

print( d2 < Dlugosc( "100 cm" ) )


