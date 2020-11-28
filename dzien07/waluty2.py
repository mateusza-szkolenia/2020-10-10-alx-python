import json
# PRZEROBIC z obslugi pliku txt na JSON

def podaj_kurs( waluta ):
    kursy = json.load(open("kursy.json"))
    return kursy[waluta]

def przelicz( kwota, waluta_z, waluta_na ):
    return kwota * podaj_kurs(waluta_z) / podaj_kurs(waluta_na)

with open("wynik.txt", "w") as wynik:
    zlecenia = json.load(open("dane.json"))
    for zlecenie in zlecenia:
        k = zlecenie['kwota']
        w1 = zlecenie['waluta-z']
        w2 = zlecenie['waluta-na']
        wynik.write(f"{k} {w1} ==> {przelicz(k, w1, w2)} {w2}\n")
