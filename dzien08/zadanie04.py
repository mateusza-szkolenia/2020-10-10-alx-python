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