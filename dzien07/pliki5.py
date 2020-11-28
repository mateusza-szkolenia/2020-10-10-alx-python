def podaj_kurs( waluta ):
    with open("kursy.txt","r") as f:
        for linia in f:
            w, k = linia.split(":")
            if w == waluta:
                return float(k)

def przelicz( kwota, waluta_z, waluta_na ):
    return kwota * KURSY[waluta_z] / KURSY[waluta_na]


kurs_EURO = podaj_kurs("EUR")
print(kurs_EURO)

#with open("dane.txt", "r") as f:
#    for linia in f:
#        k, w1, w2 = linia.split()
#        k = float(k)
#        print(f"{k} {w1} ==> {przelicz(k, w1, w2)} {w2}")
