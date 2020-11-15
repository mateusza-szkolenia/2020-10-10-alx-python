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
    def __add__(self, other):
        nowa_wartosc = self._wartosc_w_m() + other._wartosc_w_m()
        nowa_jednostka = 'm'
        return Dlugosc( nowa_wartosc, nowa_jednostka )
    def __str__(self):
        return f"{self._wartosc} {self._jednostka}"

    _mnozniki = { 'm': 1, 'km' : 1000, 'mi' : 1_609.344, 'cm' : 0.01, 'in' : 0.0254 }

d1 = Dlugosc( 2, 'mi' )
d2 = Dlugosc( 3, 'km' )

d3 = d1 + d2

print( d3 )


