napis = "ala ma kota, ola ma psa, robert ma żółwia, a ula ma chomika"

samogloski = "aeiouyó"

# ile_samoglosek = [ litera for litera in napis ]
# ile_samoglosek = [ litera for litera in napis if litera in samogloski ]
# ile_samoglosek = len( [ litera for litera in napis if litera in samogloski ] )
ile_samoglosek = len( [ None for litera in napis if litera in samogloski ] )

print(f"Samoglosek: {ile_samoglosek}")