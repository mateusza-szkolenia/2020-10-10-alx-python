import requests
import datetime
import json

def pobierz_kurs( waluta, data ):
    endDate = data
    startDate = ( datetime.date.fromisoformat(data) - datetime.timedelta(days=7) ).isoformat()
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{startDate}/{endDate}/"
    return requests.get( url ).json()['rates'][-1]['mid']

portfel = {
    "PLN" : 0
}

zlecenia = json.load( open("zlecenia.json") )

for z in zlecenia:
    dz = z['data']
    w = z['waluta']
    kurs = pobierz_kurs(w, dz)
    if w not in portfel:
        portfel[w] = 0
    if z['akcja'] == 'kup':
        portfel['PLN'] -= z['ile'] * kurs
        portfel[w] += z['ile']
    if z['akcja'] == 'sprzedaj':
        portfel['PLN'] += z['ile'] * kurs
        portfel[w] -= z['ile']
    print(z, kurs)

dzisiaj = datetime.date.today().isoformat()
for waluta, kwota in portfel.items():
    if waluta == 'PLN':
        continue
    kurs = pobierz_kurs( waluta, dzisiaj )
    portfel['PLN'] += kwota * kurs
    portfel[waluta] = 0

print(portfel)
