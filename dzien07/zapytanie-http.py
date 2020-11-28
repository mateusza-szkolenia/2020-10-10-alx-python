# wymaga poinstalowania pakietu requests za pomoca:
#
#   pip install requests
#

import requests

kurs_EUR = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json").json()['rates'][0]['mid']

print( kurs_EUR )

