# napisac program ktory poda wynik rzutu 3 kostkami (sumę)

import random

ile = 3
suma = 0
i = 0

while i < ile:
    suma += random.randint( 1, 6 )
    i += 1

print(f"Wynik rzutu 3K6: {suma}")

