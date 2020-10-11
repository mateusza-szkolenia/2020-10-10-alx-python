import random

gx = random.randint( 1, 10 )
gy = random.randint( 1, 10 )
sx = random.randint( 1, 10 )
sy = random.randint( 1, 10 )

while True:
    odleglosc = abs( gx-sx ) + abs( gy-sy )
    print(f"Twoja pozycja: {gx}, {gy} --> {odleglosc} ")
    #print(f"Pozycja skarbu: {sx}, {sy}")

    ruch = input("Ruch [NSWE]? ")
    if ruch == "N":
        gy -= 1
    elif ruch == "S":
        gy += 1
    elif ruch == "W":
        gx -= 1
    elif ruch == "E":
        gx += 1
    else:
        print("Błędny kierunek")

    if gy < 1 or gy > 10 or gx < 1 or gx > 10:
        print("Wypadłeś z planszy. GAMEOVER")
        break

    if gy == sy and gx == sx:
        print("Znalazles skarb.")
        break