miastoA = input("Miasto A:")
miastoB = input("Miasto B:")
dystans = int(input(f"Dystans {miastoA}-{miastoB}:"))
cenaPaliwa = float(input("Cena paliwa:"))
spalanie = float(input("Spalanie na 100km:"))

koszt = dystans * cenaPaliwa * spalanie / 100

print( f"Koszt przejazdu {miastoA}-{miastoB} wynosi {koszt:.2f} PLN." )
