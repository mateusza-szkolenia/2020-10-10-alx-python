zarobki = [ 4000, 6000, 3000, 9000, 20000, 7500 ]

# zalozmy ze jest podatek liniowy i chcemy policzyc podatek o wartosci 10% od kazdego z tych wynagrodzen
# obliczyc sumaryczny podatek zaplacony przez te osoby

podatek = 0

for z in zarobki:
    podatek += z * 0.1

print(f"Calkowity zebrany podatek: {podatek}")
