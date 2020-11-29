# Zaimplementuj klase Employee umozliwiajaca rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki
# godzinowej. Jezeli pracownik bedzie pracował wiecej niz 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
# jako nadgodziny (z podwójna stawka godzinowa).
# Przykład uzycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0
# >>> employee.register_time(5)
# >>> employee.register_time(5)
# >>> employee.register_time(5)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 2000.0

class Employee:
    def __init__(self, imie, nazwisko, stawka ):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stawka = stawka
        self._ile_zarobil = 0.0
    def register_time(self, time_h):
        self._ile_zarobil += self._stawka * ( time_h + ( 0 if time_h <= 8 else time_h - 8 ) )
    def pay_salary(self):
        wyplata = self._ile_zarobil
        self._ile_zarobil = 0
        return wyplata

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
x = employee.pay_salary()
print(x)
x = employee.pay_salary()
print(x)
x = employee.pay_salary()
print(x)
employee.register_time(10)
x = employee.pay_salary()
print(x)