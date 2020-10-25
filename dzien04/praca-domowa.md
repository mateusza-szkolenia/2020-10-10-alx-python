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

Zakład w systemie lotto to 6 różnych liczb z przedziału od **1** do **49** włącznie.

Wygenerować listę 100000 losowych zakładów i policzyć ile było zwycięskich trafień:
- szóstek
- piątek
- czwórek
- trójek

Czy wyniki symulacji zgadzają się z prawdopodobieństwem zwycięstwa podanym na [Wikipedii](https://pl.wikipedia.org/wiki/Lotto_(gra_liczbowa)#Prawdopodobie%C5%84stwo_trafienia_dok%C5%82adnie_k_liczb)?

