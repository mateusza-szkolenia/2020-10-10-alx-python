# Pola i Dlugosci

Zaimplementowac klasę Pole wraz ze wszystkimi operatorami i metodami:
- porównywanie
- dodawania, odejmowanie, mnozenie, dzielenie
- konstruktor


Niech mnożenie dwóch długości daje w wyniku obiekt klasy Pole, np.
```
a = Dlugosc("1 in")
b = Dlugosc("3 cm")
p = a * b
print(p) # powinno napisac

p2 = Pole( 144, 'cm2' )
print(p2) # powinno napisac "144 cm2"

p3 = p + p2
print(p3)

proporcja = p3/p1 # powinno zwrócić float

p4 = Pole( 100, 'm2')
print( p4/5 ) # powinno napisac "20 m2" 

x = Dlugosc( 3, "in" )
p5 = x**2   # obslugujemy tylko podnoszenie do potegi 2
print(p5) # powinno napisać "9 in2"
```
