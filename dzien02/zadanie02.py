liczby = []

while len( liczby ) < 10:
    x = input("Podaj liczbe lub KONIEC: ")
    if x == "KONIEC":
        break
    liczby.append( float( x ) )

if len(liczby) == 0:
    print("Pusta lista liczb")
else:
    print(f"srednia wynosi: { sum(liczby)/len(liczby) }")