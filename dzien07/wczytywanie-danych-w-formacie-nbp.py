import json

x = json.load( open( "nbp-USD.json", encoding="UTF-8" ) )
print(x)
print(x['rates'])
print(x['rates'][0])
print(x['rates'][0]['mid'])

kurs = json.load( open( "nbp-USD.json", encoding="UTF-8" ) )['rates'][0]['mid']
print(kurs)
