# Zaimplementuj klase ElectricCar odwzorowujaca zachowanie
# samochodu elektrycznego. Klasa powinna umozliwiac pokonanie
# zadanego dystansu, który nie moze przekroczyc maksymalnego
# zasiegu zdefiniowanego dla samochodu. Samochód powinien
# miec takze mozliwosc naładowania baterii.
# >>> car = ElectricCar(100)
# >>> car.drive(70)
# 70
# >>> car.drive(50)
# 30
# >>> car.drive(50)
# 0
# >>> car.charge()
# >>> car.drive(50)
# 50

class ElectricCar:
    def __init__(self, zasieg):
        self._zasieg_max = zasieg
        self.charge()
    def drive(self, dystans):
        dystans = min( (dystans, self._zasieg) )
        self._zasieg -= dystans
        print(f"Przejechano {dystans}")
    def charge(self):
        self._zasieg = self._zasieg_max
    _zasieg = 0
    _zasieg_max = 0

car = ElectricCar(100)
car.drive(70)
car.drive(50)
car.charge()
car.drive(80)
car.drive(80)
