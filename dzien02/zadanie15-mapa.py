import random

# https://repl.it/repls/ComfortableExhaustedRelationalmodel

gx = random.randint( 1, 10 )
gy = random.randint( 1, 10 )
sx = random.randint( 1, 10 )
sy = random.randint( 1, 10 )
odleglosc = abs( gx-sx ) + abs( gy-sy )

kroki = 0
maxkroki = 2 * odleglosc

while True:
    azymut = ""
    if gy < sy:
      azymut = "S"
    if gy > sy:
      azymut = "N"
    if gx < sx:
      azymut = azymut + "E"
    if gx > sx:
      azymut = azymut + "W"

    #print(f"Twoja pozycja: {gx}, {gy} --> {azymut}   {sx},{sy} ({odleglosc})")

    print('\x1b[H\x1b[J')
    y = 1
    while y <= 10:
        x = 1
        while x <= 10:
            if x == gx and y == gy:
                print("\\@/", end="")
  #          elif x == sx and y == sy:
  #              print("*", end="")
            else:
                print("...", end="")
            print(" ", end="")
            x += 1
        print("")
        y += 1
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

    nowaodleglosc = abs( gx-sx ) + abs( gy-sy )
    if nowaodleglosc > odleglosc:
      print("Zle")
    else:
      print("Dobrze")

    odleglosc = nowaodleglosc

    if gy < 1 or gy > 10 or gx < 1 or gx > 10:
        print("Wypadłeś z planszy. GAMEOVER")
        break

    if gy == sy and gx == sx:
        print("Znalazles skarb.")
        break

    if kroki == maxkroki:
        print("Nie znalazles skarbu przed zmrokiem")
        break

    kroki += 1