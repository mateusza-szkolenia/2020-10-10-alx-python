#sprawdzamy czy podany rok jest przestępny

rok = int(input("Podaj rok:"))

print("Rok przestępny:", (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0)
