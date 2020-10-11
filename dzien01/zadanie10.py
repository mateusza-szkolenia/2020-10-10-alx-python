a = int(input("Podaj pierwszą liczbę:"))
b = int(input("Podaj drugą liczbę:"))
op = input("Podaj rodzaj operacji:")

if op == "+":
    print(f"Wynik = {a + b}")
elif op == "-":
    print(f"Wynik = {a - b}")
elif op == "*":
    print(f"Wynik = {a * b}")
elif op == "/":
    if b == 0:
        print("Nie dziel przez 0!")
    else:
        print(f"Wynik = {a / b}")
else:
    print("Niepoprawna operacja!")
