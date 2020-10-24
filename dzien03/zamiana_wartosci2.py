# zamienic dwie wartosc miejscami

a = 100
b = 200

print(f"Przed: a={a} b={b}")

# sztuczka uzywana w Pythonie:
a, b = b, a

print(f"Po: a={a} b={b}")

