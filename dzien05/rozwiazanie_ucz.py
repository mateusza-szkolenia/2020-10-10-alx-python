uczniowie = [
  {"imie":"Tadeusz","nazwisko":"V.","oceny":"1 4 4 1 2 2 4 1 3 3 2 1"},
  {"imie":"Karol","nazwisko":"F.","oceny":"4 3 6 2 5 2 4 5 4 6 5 3"},
  {"imie":"Tadeusz","nazwisko":"P.","oceny":"2 1 2 2 4 3 2 1 3 2 4 4"},
  {"imie":"Mateusz","nazwisko":"O.","oceny":"5 5 4 3 2 4 3 3 3 2 5 4"},
  {"imie":"Tadeusz","nazwisko":"E.","oceny":"4 4 2 5 6 5 2 2 3 5 3 6"},
  {"imie":"Małgorzata","nazwisko":"N.","oceny":"4 5 2 1 1 3 6 3 4 5 2 5"},
  {"imie":"Ilona","nazwisko":"L.","oceny":"4 4 5 5 6 6 2 5 1 6 2 2"},
  {"imie":"Borys","nazwisko":"J.","oceny":"5 5 5 5 3 5 3 4 4 5 3 4"},
  {"imie":"Wiktoria","nazwisko":"Q.","oceny":"4 5 3 4 6 4 6 3 4 4 6 4"},
  {"imie":"Barnaba","nazwisko":"E.","oceny":"4 3 5 3 4 4 4 3 4 4 3 5"},
  {"imie":"Barnaba","nazwisko":"Z.","oceny":"5 6 6 5 4 5 3 3 5 3 4 3"},
  {"imie":"Barnaba","nazwisko":"I.","oceny":"3 4 3 3 4 3 4 3 3 3 4 3"},
  {"imie":"Halina","nazwisko":"L.","oceny":"4 5 4 6 3 4 3 3 3 4 4 4"},
  {"imie":"Marek","nazwisko":"K.","oceny":"5 5 5 4 3 6 4 4 3 4 6 3"},
  {"imie":"Halina","nazwisko":"S.","oceny":"3 4 3 4 3 4 3 3 4 4 4 3"},
  {"imie":"Joanna","nazwisko":"D.","oceny":"4 3 6 5 6 3 4 3 3 3 6 5"},
  {"imie":"Natalia","nazwisko":"G.","oceny":"5 4 3 3 4 3 3 5 4 3 3 5"},
  {"imie":"Ilona","nazwisko":"E.","oceny":"4 3 4 4 4 4 4 4 3 4 4 4"},
  {"imie":"Wiktoria","nazwisko":"T.","oceny":"3 3 3 6 3 5 5 6 4 3 6 4"},
  {"imie":"Karol","nazwisko":"M.","oceny":"4 3 3 4 4 3 3 3 4 4 3 4"},
  {"imie":"Joanna","nazwisko":"B.","oceny":"5 2 4 5 4 5 2 5 5 4 2 5"},
  {"imie":"Przemysław","nazwisko":"D.","oceny":"2 3 4 6 6 4 4 4 5 2 2 5"},
  {"imie":"Iwona","nazwisko":"V.","oceny":"2 4 1 2 2 1 3 4 1 3 3 3"},
  {"imie":"Joanna","nazwisko":"R.","oceny":"3 3 3 5 4 4 5 4 5 3 5 3"},
  {"imie":"Mateusz","nazwisko":"O.","oceny":"2 4 4 3 2 4 3 3 2 4 3 2"},
  {"imie":"Tomasz","nazwisko":"B.","oceny":"1 1 1 5 4 1 5 3 5 4 4 1"},
  {"imie":"Jacek","nazwisko":"X.","oceny":"2 2 2 2 2 4 1 3 2 5 1 6"}
]

# Wypisać wszystkich uczniów w formacie Imie Nazwisko
for uczen in uczniowie:
    print(f"{uczen['imie']} {uczen['nazwisko']}")

# Wypisać wszystkich uczniów w formacie: Nazwisko, Imie
for uczen in uczniowie:
    print(f"{uczen['nazwisko']}, {uczen['imie']}")

# Wypisać wszystkich uczniów w foramcie: Imie Nazwisko [3,4,5...] (gdzie [3,4,5...] to pełna lista ocen)
for uczen in uczniowie:
    # oceny = [ int(o) for o in uczen['oceny'].split() ]
    oceny = "[" + ",".join( uczen['oceny'].split() ) + "]"
    print(f"{uczen['nazwisko']}, {uczen['imie']} {oceny}")

# Wypisać wszystkich uczniów w formacie: Imie Nazwisko 5.4 (gdzie 5.4 to średnia ocen)
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    srednia = sum( oceny ) / len( oceny )
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {srednia:.2f}")

# Wypisać wszystkich uczniów w formacie: Imie Nazwisko (3 lepszych) (gdzie 3 to liczba uczniow z wyzsza srednia)
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    srednia = sum( oceny ) / len( oceny )
    ilu_lepszych = 0
    for u2 in uczniowie:
        o2 = [ int(o) for o in u2['oceny'].split() ]
        sr2 = sum( o2 ) / len( o2 )
        if sr2 > srednia:
            ilu_lepszych += 1

    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {srednia:.2f} (lepszych: {ilu_lepszych})")

# Wypisać wszystkich uczniów w formacie: Imie Nazwisko (3 lepszych) (gdzie 3 to liczba uczniow z wyzsza srednia)
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    srednia = sum( oceny ) / len( oceny )
    # lepsi = [ u for u in uczniowie ]
    # lepsi = [ u['oceny'] for u in uczniowie ]
    # lepsi = [ u['oceny'].split() for u in uczniowie]
    # lepsi = [ [ int(o) for o in u['oceny'].split() ] for u in uczniowie]
    # lepsi = [ [ [int(o) for o in u['oceny'].split() ] ] for u in uczniowie]   # Robimy listę list...
    # lepsi = [ [ sum(x) for x in [ [ int(o) for o in u['oceny'].split() ] ] ] for u in uczniowie]
    # lepsi = [ [ sum(x)/len(x) for x in [[int(o) for o in u['oceny'].split()]]] for u in uczniowie]
    # lepsi = [[sum(x) / len(x) for x in [[int(o) for o in u['oceny'].split()]]][0] for u in uczniowie]
    # lepsi = [ sr for sr in [ [sum(x) / len(x) for x in [[int(o) for o in u['oceny'].split()]] ][0] for u in uczniowie ] if sr > srednia ]
    lepsi = len( [ sr for sr in [[sum(x) / len(x) for x in [[int(o) for o in u['oceny'].split()]]][0] for u in uczniowie] if
             sr > srednia] )

    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {srednia:.2f} {lepsi}")

# Wypisać uczniów mających średnią powyżej 4.1 (w formacie Imie Nazwisko 4.8)

for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    srednia = sum( oceny ) / len( oceny )
    if not srednia > 4.1:
        continue
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {srednia:.2f}")

# Wypisać uczniów mających co najmniej jedną 6
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    if 6 not in oceny:
        continue
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

# Wypisać uczniów mających co najmniej jedną 5 lub 6
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    if 5 in oceny or 6 in oceny:
        print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

# Wypisać uczniów mających co najmniej jedną 5 lub 6 (2 metoda)
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    if 5 not in oceny and 6 not in oceny:
        continue
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

# Wypisać uczniów mających co najmniej jedną 1
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    if 1 not in oceny:
        continue
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

#Wypisać uczniów mających co najwyżej jedną 1 (lub wcale)
for uczen in uczniowie:
    oceny = [ int(o) for o in uczen['oceny'].split() ]
    jedynki = [ o for o in oceny if o == 1 ]
    if len( jedynki ) > 1:
        continue
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {jedynki}")

# Wypisać uczniów wraz z sumaryczną liczbą każdej z ocen 1-6, w formacie: Imie Nazwisko (1=0 2=0 3=2 4=1 5=4 6=3)
# krok roboczy
for uczen in uczniowie:
    oceny = [int(o) for o in uczen['oceny'].split()]
    for stopien in [1,2,3,4,5,6]:
        ile = len( [ o for o in oceny if o == stopien ] )
        print(f"{stopien} => {ile}")
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

# Wypisać uczniów wraz z sumaryczną liczbą każdej z ocen 1-6, w formacie: Imie Nazwisko (1=0 2=0 3=2 4=1 5=4 6=3)
# krok roboczy 2
for uczen in uczniowie:
    oceny = [int(o) for o in uczen['oceny'].split()]
    statystyka = { stopien : len( [ o for o in oceny if o == stopien ] ) for stopien in [1,2,3,4,5,6] }
    print(statystyka)
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {oceny}")

# Wypisać uczniów wraz z sumaryczną liczbą każdej z ocen 1-6, w formacie: Imie Nazwisko (1=0 2=0 3=2 4=1 5=4 6=3)

for uczen in uczniowie:
    oceny = [int(o) for o in uczen['oceny'].split()]
    statystyka = " ".join( [ str(st)+"="+str(oc) for st,oc in { stopien : len( [ o for o in oceny if o == stopien ] ) for stopien in [1,2,3,4,5,6] }.items() ])
    print(f"{uczen['imie']:10} {uczen['nazwisko']:10} {statystyka}")

# Wypisać imiona występujące w klasie wraz liczbą uczniów o tym imieniu: Imie (2)

imiona = set( [ u['imie'] for u in uczniowie ] )
for i in imiona:
    ile = len( [ u for u in uczniowie if u['imie'] == i ] )
    print(f"{i} ({ile})")
