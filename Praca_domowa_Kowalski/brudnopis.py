# class Person:
#
#     TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
#
#     def __init__(self, title, name, surname):
#         if title not in self.TITLES:
#             raise ValueError("%s is not a valid title." % title)
#
#         self.title = title
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         return f"{self.title} {self.name} {self.surname}"
# p1 = Person('r','Krystian', 'Kowalski')
#
# print(p1)

class Robot:
    def __init__(self, imie, kolor, waga):
        self._imie = imie
        self._kolor = kolor
        self._waga = waga
    def przedstaw_sie_robocie(self):
        return print(f"Cześć, jestem robotem o imieniu {self._imie}")

class Ludzie:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko
    def przedstaw_sie_czlowieku(self):
        return print(f"Cześć, jestem czlowiekiem o imieniu {self._imie}")

r1 = Robot('Krystian', 'zielony', '50')
r1.przedstaw_sie_robocie()
l1 = Ludzie('Henio', 'Szczęśliwy')
l1.przedstaw_sie_czlowieku()

l1.ma_robota = r1
l1.ma_robota.przedstaw_sie_robocie()