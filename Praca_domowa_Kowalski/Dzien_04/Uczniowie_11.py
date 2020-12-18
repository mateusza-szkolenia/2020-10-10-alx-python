uczniowie = [
  {"imie":"Tadeusz","nazwisko":"V.","oceny":"1 4 4 1 2 2 4 1 3 3 2 1"},
  {"imie":"Karol","nazwisko":"F.","oceny":"4 3 6 2 5 2 4 5 4 6 5 3"},
  {"imie":"Tadeusz","nazwisko":"P.","oceny":"2 1 2 2 4 3 2 1 3 2 4 4"},
  {"imie":"Mateusz","nazwisko":"O.","oceny":"5 5 4 3 2 4 3 3 3 2 5 4"},
  {"imie":"Tadeusz","nazwisko":"E.","oceny":"4 4 2 5 6 5 2 2 3 5 3 6"},
  {"imie":"Małgorzata","nazwisko":"N.","oceny":"4 5 2 1 1 3 6 3 4 5 2 5"},
  {"imie":"Ilona","nazwisko":"L.","oceny":"4 4 5 5 6 6 2 5 1 6 1 2"},
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
  {"imie":"Jacek","nazwisko":"X.","oceny":"2 2 2 2 2 4 1 3 2 5 1 6"},
  #### DODANI PRZEZE MNIE:
  {"imie":"Wymiatacz","nazwisko":"Sz.","oceny":"5 6 6 6 6 6 6 6 6 6 6 6"},
  {"imie":"Justyna","nazwisko":"KK.","oceny":"5 5 5 6 6 6 6 6 6 6 6 6 1"},
  {"imie":"Stanislaw","nazwisko":"KK.","oceny":"5 5 5 5 5 6 6 6 6 6 6 6"},
  {"imie":"Gerwazy", "nazwisko":"D.","oceny":"4 4 5 5 5 4 4 5 5 5 6 5 5"},
  {"imie":"Maciej", "nazwisko":"C.","oceny":"4 4 5 5 5 4 4 5 5 5 3 5 5 1"}
]
print("11. Wypisać uczniów wraz z sumaryczną liczbą każdej z ocen 1-6, w formacie: Imie Nazwisko (1=0 2=0 3=2 4=1 5=4 6=3)")
for osoba in uczniowie:
  oceny_int = [int(ocena) for ocena in osoba['oceny'] if ocena != ' ']
  jedynki = len([i for i in oceny_int if i == 1])
  dwojki = len([i for i in oceny_int if i == 2])
  trojki = len([i for i in oceny_int if i == 3])
  czworki = len([i for i in oceny_int if i == 4])
  piatki = len([i for i in oceny_int if i == 5])
  szostki = len([i for i in oceny_int if i == 6])
  print(f"{osoba['imie']}, {osoba['nazwisko']}, (1 = {jedynki}, 2 = {dwojki}, 3 = {trojki}, 4 = {czworki}, "
        f"5 = {piatki}, 6 = {szostki}")