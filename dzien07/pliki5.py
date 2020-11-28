KURSY = {
    'PLN' : 1.00,
    'EUR' : 4.48,
    'USD' : 3.75,
    'GBP' : 4.99
}

def przelicz( kwota, waluta_z, waluta_na ):
    return kwota * KURSY[waluta_z] / KURSY[waluta_na]

with open("dane.txt", "r") as f:
    for linia in f:
        k, w1, w2 = linia.split()
        k = float(k)
        print(f"{k} {w1} ==> {przelicz(k, w1, w2)} {w2}")
