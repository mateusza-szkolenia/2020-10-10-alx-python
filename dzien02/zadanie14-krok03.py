# uzytkownik podaje liczby typu float
# az do napisania slowa "koniec"
# podac najmniejsza i najwieksza z nich

najwieksza = None
najmniejsza = None

while True:
    liczba_txt = input("Podaj liczbe: ")
    if liczba_txt == "koniec":
        break

    liczba = float(liczba_txt)

    if najwieksza == None:
        najwieksza = liczba
    if najmniejsza == None:
        najmniejsza = liczba
    if liczba > najwieksza:
        najwieksza = liczba
    if liczba < najmniejsza:
        najmniejsza = liczba

print(f"min={najmniejsza}  max={najwieksza}")


