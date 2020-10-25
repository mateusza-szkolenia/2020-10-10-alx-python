# uzyc tej funkcji w glownym kodzie programu
# oraz oczyscic funkcje z niepotrzebnych komunikatow

def przelicz_temp_C( tC ):
    tF = 1.8 * tC + 32
    print(f"{tC}°C = {tF}°F")

def przelicz_C_na_F( tC ):
    tF = 1.8 * tC + 32
    return tF

pomiary = [ 12, 13, 15, 13, 10, 9, 6, 10, -1, -2, 4 ]

# zimno < 60°F
# cieplo >= 60°F

# wyswietlic tylko te pomiary kiedy jest cieplo

for tempC in pomiary:
    tempF = przelicz_C_na_F( tempC )
    print(f"{tempC}°C ===> {tempF}°F")

