liczby = [45, -33, 0, 67, 100, 2000, -1 ]

dod = []
uje = []

for n in liczby:
    if n < 0:
        uje += [ n ]
    elif n > 0:
        dod.append( n )

print( f"Dodatnie: {dod}   {len(dod)}")
print( f"Ujemne: {uje}   {len(uje)}")
