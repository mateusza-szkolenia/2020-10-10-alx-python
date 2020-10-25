imiona_meskie_a = [ "Kuba", "Barnaba" ]
imiona_zenskie_bez_a = [ "Viki", "Margaret" ]

pracownicy = [
    {
        "imie":"Mateusz",
        "nazwisko":"Adamowski",
        "stanowisko":"trener",
        "szkolenia":["Linux","Python","C","C++","IPv6"]
    },
    {
        "imie":"Jacek",
        "nazwisko":"Fiok",
        "stanowisko":"szef",
        "wzrost":1.80
    },
    {
        "imie":"Magda",
        "nazwisko":"W.",
        "stanowisko":"ksiegowosc",
        "ulubiony_kolor":["czarny"]
    },
    {
        "imie":"Agata",
        "nazwisko":"P.",
        "stanowisko":"trener",
        "szkolenia":['Python','Excel','SQL',"Access"]
    },
    {
        "imie":"Tadeusz",
        "nazwisko":"X.",
        "stanowisko":"trener",
        "szkolenia":["Excel","Access","SQL","Oracle"]
    },
    {
        "imie":"Kuba",
        "stanowisko":"admin",
        "zwolniony":2013
    },
    {
        "imie":"Kuba",
        "stanowisko":"trener",
        "nazwisko":"XXX"
    }
]

for pracownik in pracownicy:
    print( f"Pracownik: {pracownik['imie']} { pracownik['nazwisko'] if 'nazwisko' in pracownik else '***' }" )

# napisac ilu jest trenerow

ilu_trenerow = 0
for pracownik in pracownicy:
    if pracownik['stanowisko'] == 'trener':
        ilu_trenerow += 1

print(f"Trenerow: {ilu_trenerow}")

ilu_trenerow2 = len( [ 1 for p in pracownicy if p['stanowisko'] == 'trener' ] )
print(f"Trenerow: {ilu_trenerow2} ")

# napisac nazwiska trenerow mezczyzn
imiona_tren_mez = "\n".join([
    f"{p['imie']} {p['nazwisko']}"
    for p in pracownicy
    if
        p['stanowisko'] == 'trener' and (
            p['imie'] in imiona_meskie_a or (
               p['imie'][-1] != 'a'
               and p['imie'] not in imiona_zenskie_bez_a
            )
        )
])

print( f"Trenerzy mezczyzni:\n{imiona_tren_mez}" )
