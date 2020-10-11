ile_dni = 7
numer_dnia = 1
suma_temperatur = 0.0

while numer_dnia <= ile_dni:
    temperatura = float(input(f"Podaj temp. dnia {numer_dnia}: "))
    suma_temperatur += temperatura
    numer_dnia += 1

srednia_temp = suma_temperatur / ile_dni

print(f"Średnia temperatura wynosi: {srednia_temp:.1f}")
