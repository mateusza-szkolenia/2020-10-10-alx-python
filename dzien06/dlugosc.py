class Dlugosc:
    def __init__(self, wartosc, jednostka='m'):
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
        if self._jednostka == other._jednostka:
            nowa_wartosc = self._wartosc + other._wartosc
            nowa_jednostka = self._jednostka
        else:
            nowa_wartosc = self._wartosc_w_m() + other._wartosc_w_m()
            nowa_jednostka = 'm'
        return Dlugosc( nowa_wartosc, nowa_jednostka )
    def __sub__(self, other):
        return self + ( - other )
    def __mul__(self, other):
        if type( other ) in ( float, int ):
            return Dlugosc( self._wartosc * other, self._jednostka )
        return None
    def __str__(self):
        return f"{self._wartosc} {self._jednostka}"
    def __repr__(self):
        return f"Dlugosc({repr(self._wartosc)}, {repr(self._jednostka)})"
    def konwertuj_na(self, jednostka):
        return Dlugosc( self._wartosc_w_jednostce(jednostka), jednostka )
    _mnozniki = { 'm': 1, 'km' : 1000, 'mi' : 1_609.344, 'cm' : 0.01, 'in' : 0.0254 }
    __rmul__ = __mul__

#d = Dlugosc(1, 'mi')    # 1.609km => 160934 cm
#print( d._wartosc_w_jednostce('cm') )

d3 = Dlugosc( 50, 'm' )
d4 = d3.konwertuj_na('in')

print( d3 )
print( d4 ) # wypisze 1968.5039370078741 in


