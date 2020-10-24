# zamienic dwie wartosc miejscami

a = 100
b = 200

# NIE ZADZIALA!!!
# a = b     # w tym momencie bezpowrotnie tracimy wartosc a (100)
# b = a     # to juz nie mam sensu, bo w a jest juz nowa wartosc (200)

print(f"Przed: a={a} b={b}")

# prawidlowe rozwiazanie:
t = a       # zmienna tymczasowa
a = b       # wciaz mamy oryinalna wartosc a (100) w zmiennej t
b = t       # przywracamy wartosc tymczasowa do zmiennej b

print(f"Po: a={a} b={b}")
