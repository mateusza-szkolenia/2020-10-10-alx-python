with open("dane.txt", "r") as f:
    for linia in f:
        kwota, waluta1, waluta2 = linia.split()
        print(f"{kwota} {waluta1} ==> xxx {waluta2}")