import requests
import datetime
import json

def pobierz_kurs( waluta, data ):
    endDate = data
    startDate = ( datetime.date.fromisoformat(data) - datetime.timedelta(days=7) ).isoformat()
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{startDate}/{endDate}/"
    return requests.get( url ).json()['rates'][-1]['mid']

portfel = {
    "PLN" : 0,
    "EUR" : 0,
    "USD" : 0
}

zlecenia = json.load( open("zlecenia.json") )

for z in zlecenia:
    dz = z['data']
    w = z['waluta']
    kurs = pobierz_kurs(w, dz)
    print(z, kurs)
