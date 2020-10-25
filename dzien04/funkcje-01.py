# uzyc tej funkcji w glownym kodzie programu
# oraz oczyscic funkcje z niepotrzebnych komunikatow

def przelicz_temp_C( tC ):
    tF = 1.8 * tC + 32
    print(f"{tC}°C = {tF}°F")

pomiary = [ 12, 13, 15, 13, 10, 9, 6, 10, -1, -2, 4 ]

for tempC in pomiary:
    przelicz_temp_C( tempC )
