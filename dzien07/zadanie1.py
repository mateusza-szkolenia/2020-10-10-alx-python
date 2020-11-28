import requests

def pobierz_kurs( waluta, data ):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{data}/"
    wynik = requests.get( url )
    return wynik

data = "2019-12-26"
waluta = "EUR"

# chcialbym miec funkcje, ktora pobierze kurs obowiazujacy danego dnia:
# (czyli z tego dnia, lub jesli to swieto to z ostatniego roboczego)
kurs = pobierz_kurs( waluta, data )
print(kurs) # tutaj chcemy dostac liczbe float