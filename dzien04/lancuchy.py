napis = "ala ma kota a kot ma pchly"

for x in napis:
    print( f"[ {x} ]", end=" " )

print( napis.find("k") ) # podaje pozycje litery k (pierwszej!)
print( napis.find("kot") ) # podaje pozycje slowa "kot" (pierwszego!)
