class Dlugosc:
    def __init__(self, wartosc, jednostka='m'):
        self._wartosc = wartosc
        self._jednostka = jednostka
    def _wartosc_w_m(self):
        return self._wartosc * self._mnozniki[self._jednostka]
    def __lt__(self, other):
        return self._wartosc_w_m() < other._wartosc_w_m()
    def __eq__(self, other):
        return self._wartosc_w_m() == other._wartosc_w_m()
    _mnozniki = { 'm': 1, 'km' : 1000, 'mi' : 1_609.344, 'cm' : 0.01, 'in' : 0.0254 }

d1 = Dlugosc( 8000, 'm' )
d2 = Dlugosc( 8, 'km' )
d3 = Dlugosc( 2, 'mi' )

print( d1 == d2 )

