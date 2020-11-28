import datetime

d = "2020-06-05"
ile_dni = 7
d2 = (datetime.date.fromisoformat(d) - datetime.timedelta(days=ile_dni)).isoformat()

print(f"d={d}   d2={d2}")