# 1. przerobic funkcje przelicz_temp_C, aby uzywala funkcji przelicz_C_na_F
# 2. dopisac funkcje przelicz_C_na_K
# 3. przerobic funkcje przelicz_temp_C, aby wyswietla zarowno °C, °F i K
# 4. w glownym programie napisac przy kazdej tempraturze czy jest cieplo czy zimno (prog 60°F)

def przelicz_temp_C( tC ):
    tF = przelicz_C_na_F( tC )
    tK = przelicz_C_na_K( tC )
    print(f"{tC}°C = {tF}°F = {tK}K")

def przelicz_C_na_F( tC ):
    tF = 1.8 * tC + 32
    return tF

def przelicz_C_na_K( tC ):
    tK = 273.15 + tC
    return tK

pomiary = [ 12, 33, 15, 23, 10, 9, 6, 10, -1, -2, 4 ]

# zimno < 60°F
# cieplo >= 60°F

# wyswietlic tylko te pomiary kiedy jest cieplo

for tempC in pomiary:
    tempF = przelicz_C_na_F( tempC )
    tempK = przelicz_C_na_K( tempC )

    slownie = "cieplo" if tempF >= 60 else "zimno"

    print(f"{tempC}°C ===> {tempF}°F  ===> {tempK}K   {slownie} ")

