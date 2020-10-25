napis = "ala ma kota, ola ma psa, robert ma żółwia, a ula ma chomika"

samogloski = "aeiouyó"

for s in samogloski:
    ile_razy = 0
    for l in napis:
        if l == s:
            ile_razy += 1
    print(f"{s} = {ile_razy}")


# policz wystapienia kazdej samogloski oddzielnie, czyli np:
# a = 12
# i = 2
# etc

