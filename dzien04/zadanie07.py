napis = "ala ma kota, ola ma psa, a ula ma chomika"

ile_samoglosek = 0

for litera in napis:
    if litera == "a":
        ile_samoglosek += 1
    elif litera == "e":
        ile_samoglosek += 1
    elif litera == "i":
        ile_samoglosek += 1
# i tak dalej

print(f"Samoglosek: {ile_samoglosek}")