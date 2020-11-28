import requests
import datetime

def pobierz_kurs( waluta, data ):
    endDate = data
    startDate = ( datetime.date.fromisoformat(data) - datetime.timedelta(days=7) ).isoformat()
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{startDate}/{endDate}/"
    wynik = requests.get( url )
    return wynik

data = "2019-12-26"
waluta = "EUR"

# chcialbym miec funkcje, ktora pobierze kurs obowiazujacy danego dnia:
# (czyli z tego dnia, lub jesli to swieto to z ostatniego roboczego)
kurs = pobierz_kurs( waluta, data )
print(kurs) # tutaj chcemy dostac liczbe float