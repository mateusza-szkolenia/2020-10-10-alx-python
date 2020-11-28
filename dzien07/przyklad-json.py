import json

pracownik = json.load(open("p1.json"))

print(f"imie: {pracownik['imie']}")
print(pracownik)
