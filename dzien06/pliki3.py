import random

# zapis na koncu pliku (typowe zastosowanie: raporty, logi itp)

# a = append
f = open("raport.txt", "a")
f.write("Dzisiejsza liczba: " + str(random.randint(1,10000)) + "\n")
f.close()
