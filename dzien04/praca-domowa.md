# Uczniowie

Poniższe zadania należy wykonać używając poniższej bazy uczniów:

```
uczniowie = [
    { "imie" : "Piotr", "nazwisko" : "ABC", "oceny" : [3, 6, 5, 6, 4, 3, 6, 4] },
    { "imie" : "Basia", "nazwisko" : "Tralala", "oceny" : [5, 5, 5, 6, 5, 6, 6, 6] },
    { "imie" : "Kasia", "nazwisko" : "Trututu", "oceny" : [1, 2, 5, 5, 2, 4, 5, 3] },
    { "imie" : "Jan", "nazwisko" : "Mimi", "oceny" : [3, 3, 3, 3, 5, 5, 4, 6] },
    { "imie" : "Zygmunt", "nazwisko" : "Gagaga", "oceny" : [3, 4, 4, 5, 4, 4, 3, 5] },
    { "imie" : "Andrzej", "nazwisko" : "Lolo", "oceny" : [2, 3, 5, 5, 5, 3, 4, 4] },
    { "imie" : "Piotr", "nazwisko" : "Rororo", "oceny" : [5, 6, 5, 5, 5, 6, 6, 6] },
    { "imie" : "Piotr", "nazwisko" : "Dudu", "oceny" : [4, 1, 1, 3, 1, 6, 1, 1] }
]
```

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
    { "data" : 1065, "droga" : 56165.7, "paliwo" : 66.51, "cena" : 4.91 },
    { "data" : 1068, "droga" : 56617.0, "paliwo" : 42.53, "cena" : 4.58 },
    { "data" : 1074, "droga" : 57155.8, "paliwo" : 45.85, "cena" : 4.79 },
    { "data" : 1082, "droga" : 57748.0, "paliwo" : 46.66, "cena" : 4.82 },
    { "data" : 1090, "droga" : 58302.2, "paliwo" : 61.06, "cena" : 4.60 },
    { "data" : 1098, "droga" : 58762.9, "paliwo" : 41.77, "cena" : 4.93 },
    { "data" : 1106, "droga" : 59245.9, "paliwo" : 37.67, "cena" : 4.68 },
    { "data" : 1110, "droga" : 59694.7, "paliwo" : 40.37, "cena" : 4.63 },
    { "data" : 1114, "droga" : 60392.4, "paliwo" : 61.07, "cena" : 4.65 },
    { "data" : 1120, "droga" : 61003.3, "paliwo" : 65.46, "cena" : 4.76 },
    { "data" : 1123, "droga" : 61584.1, "paliwo" : 54.83, "cena" : 4.97 },
    { "data" : 1128, "droga" : 62232.5, "paliwo" : 69.91, "cena" : 4.63 },
    { "data" : 1133, "droga" : 62654.4, "paliwo" : 32.44, "cena" : 4.74 },
    { "data" : 1138, "droga" : 63281.5, "paliwo" : 69.13, "cena" : 4.95 },
    { "data" : 1142, "droga" : 63796.1, "paliwo" : 55.94, "cena" : 4.93 },
    { "data" : 1148, "droga" : 64295.4, "paliwo" : 41.23, "cena" : 4.80 },
    { "data" : 1153, "droga" : 64922.8, "paliwo" : 55.32, "cena" : 4.94 },
    { "data" : 1159, "droga" : 65351.3, "paliwo" : 43.00, "cena" : 4.67 },
    { "data" : 1167, "droga" : 65848.5, "paliwo" : 45.08, "cena" : 4.81 },
    { "data" : 1173, "droga" : 66445.3, "paliwo" : 58.65, "cena" : 4.65 },
]

```

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

# Pętle, tablice

## Kalkulator RPN

Stworzyć funkcję obliczającą wartość wyrażenia zapisanego w [Odwrotnej notacji polskiej](https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska).

Przykład: `4 5 + 3 * 1 +` równa się `28`

Przykład: `2 7 + 3 / 14 3 - 4 * + 2 /` równa się `23.5`




