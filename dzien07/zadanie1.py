
data = "2019-12-26"
waluta = "EUR"

# chcialbym miec funkcje, ktora pobierze kurs obowiazujacy danego dnia:
# (czyli z tego dnia, lub jesli to swieto to z ostatniego roboczego)
kurs = pobierz_kurs( waluta, data )