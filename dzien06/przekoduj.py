f = open("pliterki2.txt","r", encoding="cp1250")
zawartosc = f.readlines()

with open("pliterki2-poprawione.txt", "w", encoding="UTF-8") as f2:
    f2.writelines( zawartosc )
