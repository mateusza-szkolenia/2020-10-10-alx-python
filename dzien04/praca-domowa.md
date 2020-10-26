# Uczniowie

Poniższe zadania należy wykonać używając poniższej bazy uczniów:

```
uczniowie = [
  {"imie":"Tadeusz","nazwisko":"V.","oceny":"1 4 4 1 2 2 4 1 3 3 2 1"},
  {"imie":"Karol","nazwisko":"F.","oceny":"4 3 6 2 5 2 4 5 4 6 5 3"},
  {"imie":"Tadeusz","nazwisko":"P.","oceny":"2 1 2 2 4 3 2 1 3 2 4 4"},
  {"imie":"Mateusz","nazwisko":"O.","oceny":"5 5 4 3 2 4 3 3 3 2 5 4"},
  {"imie":"Tadeusz","nazwisko":"E.","oceny":"4 4 2 5 6 5 2 2 3 5 3 6"},
  {"imie":"Małgorzata","nazwisko":"N.","oceny":"4 5 2 1 1 3 6 3 4 5 2 5"},
  {"imie":"Ilona","nazwisko":"L.","oceny":"4 4 5 5 6 6 2 5 1 6 1 2"},
  {"imie":"Borys","nazwisko":"J.","oceny":"5 5 5 5 3 5 3 4 4 5 3 4"},
  {"imie":"Wiktoria","nazwisko":"Q.","oceny":"4 5 3 4 6 4 6 3 4 4 6 4"},
  {"imie":"Barnaba","nazwisko":"E.","oceny":"4 3 5 3 4 4 4 3 4 4 3 5"},
  {"imie":"Barnaba","nazwisko":"Z.","oceny":"5 6 6 5 4 5 3 3 5 3 4 3"},
  {"imie":"Barnaba","nazwisko":"I.","oceny":"3 4 3 3 4 3 4 3 3 3 4 3"},
  {"imie":"Halina","nazwisko":"L.","oceny":"4 5 4 6 3 4 3 3 3 4 4 4"},
  {"imie":"Marek","nazwisko":"K.","oceny":"5 5 5 4 3 6 4 4 3 4 6 3"},
  {"imie":"Halina","nazwisko":"S.","oceny":"3 4 3 4 3 4 3 3 4 4 4 3"},
  {"imie":"Joanna","nazwisko":"D.","oceny":"4 3 6 5 6 3 4 3 3 3 6 5"},
  {"imie":"Natalia","nazwisko":"G.","oceny":"5 4 3 3 4 3 3 5 4 3 3 5"},
  {"imie":"Ilona","nazwisko":"E.","oceny":"4 3 4 4 4 4 4 4 3 4 4 4"},
  {"imie":"Wiktoria","nazwisko":"T.","oceny":"3 3 3 6 3 5 5 6 4 3 6 4"},
  {"imie":"Karol","nazwisko":"M.","oceny":"4 3 3 4 4 3 3 3 4 4 3 4"},
  {"imie":"Joanna","nazwisko":"B.","oceny":"5 2 4 5 4 5 2 5 5 4 2 5"},
  {"imie":"Przemysław","nazwisko":"D.","oceny":"2 3 4 6 6 4 4 4 5 2 2 5"},
  {"imie":"Iwona","nazwisko":"V.","oceny":"2 4 1 2 2 1 3 4 1 3 3 3"},
  {"imie":"Joanna","nazwisko":"R.","oceny":"3 3 3 5 4 4 5 4 5 3 5 3"},
  {"imie":"Mateusz","nazwisko":"O.","oceny":"2 4 4 3 2 4 3 3 2 4 3 2"},
  {"imie":"Tomasz","nazwisko":"B.","oceny":"1 1 1 5 4 1 5 3 5 4 4 1"},
  {"imie":"Jacek","nazwisko":"X.","oceny":"2 2 2 2 2 4 1 3 2 5 1 6"}
]
```
Więcej danych testowych można wygenerować pod adresem: 
https://mateusza2.github.io/Programowanie/Generatory/uczniowie.html


1. Wypisać wszystkich uczniów w formacie `Imie Nazwisko`
2. Wypisać wszystkich uczniów w formacie: `Nazwisko, Imie`
3. Wypisać wszystkich uczniów w foramcie: `Imie Nazwisko [3,4,5...]` (gdzie [3,4,5...] to pełna lista ocen)
4. Wypisać wszystkich uczniów w formacie: `Imie Nazwisko 5.4` (gdzie 5.4 to średnia ocen)
5. Wypisać wszystkich uczniów w formacie: `Imie Nazwisko (3 lepszych)` (gdzie 3 to liczba uczniow z wyzsza srednia)
6. Wypisać uczniów mających średnią powyżej 4.7 (w formacie `Imie Nazwisko 4.8`)
7. Wypisać uczniów mających co najmniej jedną 6
8. Wypisać uczniów mających co najmniej jedną 5 lub 6
9. Wypisać uczniów mających co najmniej jedną 1
10. Wypisać uczniów mających co najwyżej jedną 1 (lub wcale)
11. Wypisać uczniów wraz z sumaryczną liczbą każdej z ocen 1-6, w formacie: `Imie Nazwisko (1=0 2=0 3=2 4=1 5=4 6=3)`
12. Wypisać imiona występujące w klasie wraz liczbą uczniów o tym imieniu: `Imie (2)`

# Lotto

Zakład w grze Lotto to 6 różnych liczb z przedziału od **1** do **49** włącznie.

Wygenerować losowo:
- listę 100000 zakładów
- zwycięską kombinację

Policzyć ile było zwycięskich trafień:
- szóstek
- piątek
- czwórek
- trójek

Porównać, czy wyniki symulacji zgadzają się z prawdopodobieństwem zwycięstwa podanym na [Wikipedii](https://pl.wikipedia.org/wiki/Lotto_(gra_liczbowa)#Prawdopodobie%C5%84stwo_trafienia_dok%C5%82adnie_k_liczb)?

# Paliwo

Poniższa lista zawiera odnotowane tankowania samochodu:

```
tankowania = [
  {"data":1491,"droga":68186,"paliwo":47.36,"cena":5.05},
  {"data":1502,"droga":68633,"paliwo":47.46,"cena":5},
  {"data":1504,"droga":69062,"paliwo":45.71,"cena":4.35},
  {"data":1510,"droga":69631,"paliwo":42.43,"cena":4.95},
  {"data":1517,"droga":70084,"paliwo":45.07,"cena":4.43},
  {"data":1531,"droga":70620,"paliwo":42.46,"cena":4.51},
  {"data":1550,"droga":71490,"paliwo":53.33,"cena":4.98},
  {"data":1566,"droga":71887,"paliwo":42.88,"cena":4.61},
  {"data":1585,"droga":72380,"paliwo":43.12,"cena":4.31},
  {"data":1592,"droga":72758,"paliwo":43.08,"cena":4.43},
  {"data":1597,"droga":73540,"paliwo":54.14,"cena":4.95},
  {"data":1610,"droga":74039,"paliwo":46.41,"cena":4.91},
  {"data":1625,"droga":74563,"paliwo":36.48,"cena":4.89},
  {"data":1638,"droga":75077,"paliwo":47.09,"cena":4.92},
  {"data":1652,"droga":75654,"paliwo":47.55,"cena":4.32},
  {"data":1661,"droga":76358,"paliwo":52.14,"cena":4.92},
  {"data":1664,"droga":76725,"paliwo":39.48,"cena":4.81},
  {"data":1683,"droga":77064,"paliwo":39.07,"cena":4.49},
  {"data":1696,"droga":77671,"paliwo":51.13,"cena":5.05},
  {"data":1705,"droga":78064,"paliwo":45.19,"cena":4.58}
]
```

Więcej danych testowych można wygenerować pod adresem:
https://mateusza2.github.io/Programowanie/Generatory/tankowania.html

1. Policzyć spalanie dla każdego tankowania.
2. Policzyć koszt 1km dla każdego tankowania.
3. Znaleźć numer tankowania gdzie koszt był najniższy i najwyższy.
4. Policzyć średni koszt przejechania 1km w całej zarejestrowanej bazie.
5. Policzyć średnie spalanie w całej zarejestrowanej bazie.
6. Policzyć średni koszt dzienny.

# Wartości losowe

Zasymulować 10 rzutów kością 6-ścienną i przedstawić w postaci tekstowych wykresów uzyskane wyniki, np.

Jeśli wypadły wartości: `[ 1, 3, 2, 3, 3, 6, 5, 6, 1, 2]` to wykres powinnien wyglądać np. tak:
```
    1: XX   (2)
    2: XX   (2)
    3: XXX  (3)
    4:      (0)
    5: X    (1)
    6: XX   (2)
``` 

Zasymulować 100000 rzutów 3 kośćmi 6-ściennymi i analogicznie przedstawić sumę wyników:

```
    3: XXXX...
    2: XXXXXX...
    ...
    17: XXX
    18: X ..
```

Napisać funkcję `symuluj_rzuty( a, b, c )`, która symuluje `a` rzutów wykonanych za pomocą `b` kości o `c` ścianach każda i rysuje wykres.


# Wyrażenia listowe itp

## Stawki VAT

Napisać wyrażenie konwertujące listę stawek VAT ze stringa postaci `A=23 B=8 C=0` na słownik postaci: `{ "A" : 23.0, "B" : 8.0, "C" : 0.0 }`

