napis = "ala ma kota, ola ma psa, robert ma żółwia, a ula ma chomika"

samogloski = "aeiouyóąę"

for s in samogloski:
    ile_razy = len( [ 1 for l in napis if l == s ] )
    if ile_razy == 0:
        continue
    print(f"{s} = {ile_razy}")

# policz wystapienia kazdej samogloski oddzielnie, czyli np:
# a = 12
# i = 2
# etc

