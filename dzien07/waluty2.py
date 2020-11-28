import json
# PRZEROBIC z obslugi pliku txt na JSON

def podaj_kurs( waluta ):
    kursy = json.load(open("kursy.json"))
    return kursy[waluta]

def przelicz( kwota, waluta_z, waluta_na ):
    return kwota * podaj_kurs(waluta_z) / podaj_kurs(waluta_na)

with open("dane.txt", "r") as dane, open("wynik.txt", "w") as wynik:
    for linia in dane:
        k, w1, w2 = linia.split()
        k = float(k)
        wynik.write(f"{k} {w1} ==> {przelicz(k, w1, w2)} {w2}\n")
