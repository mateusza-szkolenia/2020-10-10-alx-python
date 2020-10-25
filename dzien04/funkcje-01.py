# uzyc tej funkcji w glownym kodzie programu (2 petle)
# oraz oczyscic funkcje z niepotrzebnych komunikatow

def przelicz_temp_C( tC ):
    print("Dzien dobry")
    tF = 1.8 * tC + 32
    print(f"{tC}C = {tF}F")
    print("KONIEC FUNKCJI")

pomiary = [ 12, 13, 15, 13, 10, 9, 6, 10, -1, -2, 4 ]

for tempC in pomiary:
    tempF = 1.8 * tempC + 32
    print(f"{tempC}°C = {tempF}°F")

przelicz_temp_C( 10 )

pomiary = [ 10, 23, 15 ]
for tempC in pomiary:
    tempF = 1.8 * tempC + 32
    print(f"{tempC}°C = {tempF}°F")
