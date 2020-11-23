class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"{self.title} {self.name} {self.surname}"
p1 = Person('r','Krystian', 'Kowalski')

print(p1)