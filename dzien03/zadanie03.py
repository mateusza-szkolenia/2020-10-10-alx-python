liczby = [45, -33, 0, 67, 100, 2000, -1 ]

dod = 0
uje = 0

for n in liczby:
    if n < 0:
        uje += 1
    elif n > 0:
        dod += 1

print( f"Dodatnie: {dod}")
print( f"Ujemne: {uje} ")