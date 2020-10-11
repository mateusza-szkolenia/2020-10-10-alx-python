# uzytkownik podaje 5 liczb (nieujemnych)
# podac najmniejsza z nich

najmniejsza = 0
i = 0
ile = 5

while i < ile:
    liczba = float( input(f"Podaj liczbe #{i}: ") )
    if i == 0 or liczba < najmniejsza:
        najmniejsza = liczba
    i += 1

print(f"Najmniejsza z liczb to: {najmniejsza}")

