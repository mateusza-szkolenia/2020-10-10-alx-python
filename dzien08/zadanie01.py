# >>> product = Product(1, 'Woda', 10.99)
# >>> product.print_info()
# Produkt "Woda", id: 1, cena: 10.99 PLN

class Produkt():
    def __init__ (self, id, nazwa, cena):
        self._id = id
        self._nazwa = nazwa
        self._cena = cena
    def __str__(self):
        return f'Produkt: {self._nazwa}, id: {self._id}, cena {self._cena} PLN'

produkt1 = Produkt(1, 'Chleb', 2.99)
produkt2 = Produkt(2, 'Mleko', 1.99)
produkt3 = Produkt(3, 'Parówki', 4.99)

for p in produkt1, produkt2, produkt3:
    print(p)