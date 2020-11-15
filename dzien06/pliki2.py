import random

# otwiera plik do zapisu - KASUJAC CALA ZAWARTOSC
f = open("wynik.txt", "w")

# zapisuje tekst do pliku
f.write("ala ma kota " + str(random.randint(1,100000) ) + "\n" )
f.close()
