f = open("dane.txt","r")

pierwsza_linia = f.readline()
print(f"surowa linia wczytana z pliku (zawiera niepozadany znak enter): [{pierwsza_linia}]")

druga_linia = f.readline().strip()
print(f"po uzyciu .strip(): [{druga_linia}]")

f.seek(0)
# przesun kursor na poczatek pliku
naglowek = f.read(6) # wczytaj pierwsze 6 znakow

f.seek(2)
# przesun kursor na 2 bajt od poczatku
print(f.read(6)) # wyswietl 6 znakow od biezacego miejsca

#itd