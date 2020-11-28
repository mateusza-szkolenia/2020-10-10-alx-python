# Zadanie

Napisac program, który:
1. wczyta z pliku `zlecenia.json` listę zleceń wymiany walut w postaci:
```
[
    { "data" : "2020-10-01", "akcja" : "kup", "ile" : 20.00, "waluta" : "EUR" },
    { "data" : "2020-10-06", "akcja" : "sprzedaj", "ile" : 10.00, "waluta" : "EUR" },
    { "data" : "2020-10-07", "akcja" : "sprzedaj", "ile" : 1.00, "waluta" : "EUR" },
    { "data" : "2020-10-08", "akcja" : "kup", "ile" : 100.00, "waluta" : "USD" },
    { "data" : "2020-10-09", "akcja" : "sprzedaj", "ile" : 3.00, "waluta" : "USD" },
    { "data" : "2020-10-10", "akcja" : "sprzedaj", "ile" : 10.00, "waluta" : "USD" }
]
```
Uwzględniamy notowania z danego dnia, lub ostatniego dnia roboczego.

Zakładamy, że na koniec przeliczamy wszystkie posiadane waluty obce na PLN wg bieżącego kursu.

2. Wypisze do pliku `podsumowanie.txt` treść w formacie:
```
[opcjonalnie wszystkie transakcje]
Bilans: +56.34 PLN
```