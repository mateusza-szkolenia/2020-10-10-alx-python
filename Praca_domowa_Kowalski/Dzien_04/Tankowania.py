tankowania = [
  {"data":1491,"droga":68186,"paliwo":47.36,"cena":5.05},
  {"data":1502,"droga":68633,"paliwo":47.46,"cena":5},
  {"data":1504,"droga":69062,"paliwo":45.71,"cena":4.35},
  {"data":1510,"droga":69631,"paliwo":42.43,"cena":4.95},
  {"data":1517,"droga":70084,"paliwo":45.07,"cena":4.43},
  {"data":1531,"droga":70620,"paliwo":42.46,"cena":4.51},
  {"data":1550,"droga":71490,"paliwo":53.33,"cena":4.98},
  {"data":1566,"droga":71887,"paliwo":42.88,"cena":4.61},
  {"data":1585,"droga":72380,"paliwo":43.12,"cena":4.31},
  {"data":1592,"droga":72758,"paliwo":43.08,"cena":4.43},
  {"data":1597,"droga":73540,"paliwo":54.14,"cena":4.95},
  {"data":1610,"droga":74039,"paliwo":46.41,"cena":4.91},
  {"data":1625,"droga":74563,"paliwo":36.48,"cena":4.89},
  {"data":1638,"droga":75077,"paliwo":47.09,"cena":4.92},
  {"data":1652,"droga":75654,"paliwo":47.55,"cena":4.32},
  {"data":1661,"droga":76358,"paliwo":52.14,"cena":4.92},
  {"data":1664,"droga":76725,"paliwo":39.48,"cena":4.81},
  {"data":1683,"droga":77064,"paliwo":39.07,"cena":4.49},
  {"data":1696,"droga":77671,"paliwo":51.13,"cena":5.05},
  {"data":1705,"droga":78064,"paliwo":45.19,"cena":4.58}
]

def koszt_tankowania(t):
    koszt = t['paliwo'] * t['cena'] / t['droga'] * 1000
    return koszt

def srednie_spalanie(t):
    spalanie = t['paliwo']/t['droga'] * 1000
    return spalanie

pomiar = 0
koszt_max = None
koszt_min = None
for t in tankowania:
  pomiar +=1
  koszt = koszt_tankowania(t)
  if koszt_min == None or koszt_min > koszt:
    koszt_min = koszt
  if koszt_max == None or koszt_max < koszt:
    koszt_max = koszt

  print(f"{pomiar:2}. Koszt tank: {koszt:.2f}")

print(f"MIN: {koszt_min:.2f}, MAX: {koszt_max:.2f}")