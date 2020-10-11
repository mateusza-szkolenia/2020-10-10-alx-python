# uzytkownik podaje 5 liczb (nieujemnych)
# podac najwieksza z nich

najwieksza = 0
i = 0
ile = 5

while i < ile:
    liczba = float( input(f"Podaj liczbe #{i}: ") )
    if liczba > najwieksza:
        najwieksza = liczba
    else:
        # nic sie nie dzieje
        pass
    i += 1

print(f"Najwieksza z liczb to: {najwieksza}")

