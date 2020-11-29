# Zadanie #4
# Zaimplementuj klase Basket umozliwiajaca dodawanie produktów w
# okreslonej liczbie do koszyka. Zaimplementuj metode obliczajaca
# całkowita wartosc koszyka oraz wypisujaca informacje o zawartosci
# koszyka. Dodanie dwa razy tego samego produktu do koszyka
# powinno stworzyc tylko jedna pozycje.
# Przykład uzycia:
# >>> basket = Basket()
# >>> product = Product(1, 'Woda', 10.00)
# >>> basket.add_product(product, 5)
# >>> basket.count_total_price()
# 50.0
# >>> basket.generate_report()
# 'Produkty w koszyku:\n
# - Woda (1), cena: 10.00 x 5\n
# W sumie: 50.00'

class Product_in_basket:
     def __init__(self, p, n):
         self.product = p
         self.n = n
     def __str__(self):
         return f"- {self.product} x {self.n}"

class Basket:
    _products = []

    def find_product(self, product):
        for p in self._products:
            if p.product._id == product._id:
                return p
        return None

    def add_product(self, product, n):
        xxx = self.find_product( product )
        if xxx == None:
            self._products.append( Product_in_basket( product, n) )
        else:
            xxx.n += n

    def generate_report(self):
        return "Produkty w koszyku:\n" + "\n".join( [ str(x) for x in self._products ] ) + "\n" + f"Koszt: {self.count_total_price()}"
    def count_total_price(self):
        suma = 0
        for p in self._products:
            prod = p.product
            ilosc = p.n
            cena = prod._cena
            suma += cena * ilosc
        return suma

class Product:
    def __init__(self, id, nazwa, cena ):
        self._id = id
        self._nazwa = nazwa
        self._cena = cena
    def __str__(self):
        return f"{self._nazwa} ({self._id}), cena: {self._cena}"

b1 = Basket()
b1.add_product( Product( 101, "woda", 2.00 ), 7 )
b1.add_product( Product( 102, "pączek", 3.00 ), 10 )
b1.add_product( Product( 101, "woda", 2.00 ), 10 )
b1.add_product( Product( 103, "Piwo", 5.00 ), 1 )
print( b1.generate_report() )


