import requests
import json

j = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json").json()

print( j )

wpis = {
    'waluta' : j['code'],
    'kurs' : j['rates'][0]['mid'],
    'nazwa_waluty' : j['currency'],
}
print("wpis jako słownik pythona:")
print(wpis)

print("wpis jako string JSON:")
print(json.dumps(wpis, indent=4))

print("zapis do pliku:")
# nic sie nie wyswietli, bo tresc leci prosto do pliku
json.dump(wpis, open("waluta-po-mojemu.json", "w"), indent=4 )
print("KONIEC")


