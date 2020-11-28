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

class Pole:
    def __init__(self, wartosc, jednostka='m2'):
        if type(wartosc) == str:
            a, b = (wartosc+" "+jednostka).split()[0:2]
            wartosc, jednostka = float(a), b
        self._wartosc = wartosc
        self._jednostka = jednostka
    def _wartosc_w_m2(self):
        return self._wartosc * self._mnozniki[self._jednostka]
    def _wartosc_w_jednostce(self, jednostka):
        return self._wartosc_w_m2() / self._mnozniki[jednostka]
    def __lt__(self, other):
        return self._wartosc_w_m2() < other._wartosc_w_m2()
    def __eq__(self, other):
        return self._wartosc_w_m2() == other._wartosc_w_m2()
    def __neg__(self):
        return -1 * self
    def __add__(self, other):
        if type(other) == Pole:
            return Pole(
                self._wartosc + (
                    other._wartosc
                    if self._jednostka == other._jednostka
                    else other._wartosc_w_jednostce( self._jednostka )
                ),
                self._jednostka
            )
        elif type(other) in (int,float):
            # mam mieszane uczucia, czy klasa powinna sie tak zachowywac :-)
            return Pole( self._wartosc + other, self._jednostka )
        else:
            return None
    def __truediv__(self, other):
        if type(other) == Pole:
            return self._wartosc_w_m2() / other._wartosc_w_m2()
        elif type(other) in (int, float):
            return Pole( self._wartosc / other, self._jednostka )
        else:
            return None
    def __sub__(self, other):
        return self + ( - other )
    def __mul__(self, other):
        if type( other ) in ( float, int ):
            return Pole( self._wartosc * other, self._jednostka )
        return None
    #def __str__(self):
    #    return f"{self._wartosc:.1f} {self._jednostka}"
    def __repr__(self):
        return f"Pole({repr(self._wartosc)}, {repr(self._jednostka)})"
    def konwertuj_na(self, jednostka):
        return Pole( self._wartosc_w_jednostce(jednostka), jednostka )
    _mnozniki = { 'm2': 1, 'km2' : 1000**2, 'mi2' : 1_609.344**2, 'cm2' : 0.01**2, 'in2' : 0.0254**2, 'mm2' : 0.001**2, 'dm2' : 0.1**2, 'ft2' : 0.3048**2 }
    __rmul__ = __mul__


p1 = Pole( "3 m2" )
p2 = Pole( 4000, "cm2" )
p3 = p1 + p2
print(p1,p2,p3)
print(repr(p3))