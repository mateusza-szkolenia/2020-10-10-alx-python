#Napisać wyrażenie konwertujące listę stawek VAT ze stringa postaci
#A=23 B=8 C=0 na słownik postaci: { "A" : 23.0, "B" : 8.0, "C" : 0.0 }

stawki2 = "A=23 B=8 C=0 D=40"

def konwerter_string_VAT(lancuch):
    slownik = {}
    a = lancuch.split()
    for i in a:
         b = i.split("=")
         for j in b[0]:
             slownik[j] = float(b[1])
    print(slownik)

konwerter_string_VAT(stawki2)