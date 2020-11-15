import random

with open("raport.txt", "a") as f:
    f.write("Dzisiejsza liczba: " + str(random.randint(1,10000)) + "\n")
    f.write("Dzisiejsza druga liczba: " + str(random.randint(1, 10000)) + "\n")
    f.write("Dzisiejsza trzecia liczba: " + str(random.randint(1, 10000)) + "\n")
