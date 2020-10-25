# 1. przerobic funkcje przelicz_temp_C, aby uzywala funkcji przelicz_C_na_F
# 2. dopisac funkcje przelicz_C_na_K
# 3. przerobic funkcje przelicz_temp_C, aby wyswietla zarowno °C, °F i K
# 4. w glownym programie napisac przy kazdej tempraturze czy jest cieplo czy zimno (prog 60°F)

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
    print(f"{tempC}°C ===> {tempF}°F   XXXXX")

