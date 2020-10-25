napis = "ala ma kota, ola ma psa, robert ma żółwia, a ula ma chomika"
samogloski = "aeiouyóąę"

statystyki = [
    (
        s,
        len( [ None for l in napis if l == s ] )
    )
    for s in samogloski
    if s in napis
]

for samogloska, wystapienia in statystyki:
    print(f"{samogloska} = {wystapienia}")
