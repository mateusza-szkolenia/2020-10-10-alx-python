napis = "Ala ma kota, Ola ma psa, Robert ma żółwia, a Ula ma chomika"

samogloski = "aeiouyó"

# policz wystapienia

# ile_samoglosek = [ litera for litera in napis ]
# ile_samoglosek = [ litera for litera in napis if litera in samogloski ]
# ile_samoglosek = len( [ litera for litera in napis if litera in samogloski ] )
ile_samoglosek = len( [ None for litera in napis if litera.lower() in samogloski ] )

print(f"Samoglosek: {ile_samoglosek}")