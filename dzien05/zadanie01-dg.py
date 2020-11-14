def czy_jest_pierwsza(liczba):
    dzielniki = []

    for i in range(2, liczba + 1):
        if liczba % i == 0:
            dzielniki.append(i)
    print(dzielniki)

    print("Liczba pierwsza") if len(dzielniki) == 1 else print("Nie jest pierwsza")

czy_jest_pierwsza(int(input("Sprawdź czy liczba jest pierwsza: ")))