def wypisz( cos ):
    for i in cos:
        print(f"* element: {i}")
    print("I jeszcze raz:")
    for i in cos:
        print(f"* znowu: {i}")
    print("KONIEC")

imiona = ['Mateusz','Magda','Andrzej']

wypisz( list( enumerate( imiona ) ) )
