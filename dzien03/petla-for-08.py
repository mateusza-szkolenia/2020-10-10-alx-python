zarobki = [ 4000, 6000, 3000, 9000, 20000, 7500 ]

# wprowadzamy stawki:
# 15% dla zarabiajacych >= 4500
# 5% dla pozostalych

podatek = 0

# POPRAWIC

for z in zarobki:
    if z <= 4200:
        pass
    else:
        podatek += z * 0.15

print(f"Calkowity zebrany podatek: {podatek}")
