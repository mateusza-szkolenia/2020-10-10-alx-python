import random

class NPC:
    def __init__(self):
        self.name = random.choice( self.imiona )
        self.klasa = random.choice( list( self.klasy.keys() ) )
        self.poziom = 1
        self.dext = 0
        self.str = 0
        self.intel = 0
        self.HP = 0
        self.MP = 0
        self.defense = 0
        self.mdefense = 0
        self.dodge = 0
        self.xpoz = random.randint(1, 10)
        self.ypoz = random.randint(1, 10)

        self.infoklasy = {}
        self.update()

    def update(self):
        self.infoklasy = self.klasy[self.klasa]

        self.dext = self.poziom * self.infoklasy["dext"]
        self.str = self.poziom * self.infoklasy["str"]
        self.intel = self.poziom * self.infoklasy["intel"]
        self.HP = self.poziom * self.infoklasy["HP"] + self.poziom * self.infoklasy["str"]
        self.MP = self.poziom * self.infoklasy["MP"] + self.poziom * self.infoklasy["intel"]
        self.defense = self.poziom * self.infoklasy["str"] * 0.7
        self.mdefense = self.poziom * self.infoklasy["intel"] * 0.7
        self.dodge = self.poziom * self.infoklasy["dext"] * 0.7

    def move(self):
        npcMove = random.randint(1, 4)

        if npcMove == 1 and self.xpoz + 1 <= 10:
            self.xpoz += 1

        elif npcMove == 2 and self.xpoz - 1 >= 1:
            self.xpoz -= 1

        elif npcMove == 3 and self.ypoz + 1 <= 10:
            self.ypoz += 1

        elif npcMove == 4 and self.ypoz - 1 > 1:
            self.ypoz -= 1

    klasy = {
        'war' : {'classname': 'war', 'HP': 100, 'MP': 60, 'dext': 2, 'str': 4, 'intel': 2},
        'mag' : {'classname': 'mag', 'HP': 70, 'MP': 90, 'dext': 4, 'str': 1, 'intel': 4},
        'thi' : {'classname': 'thi', 'HP': 80, 'MP': 80, 'dext': 7, 'str': 2, 'intel': 2}
    }

    imiona = ["Azog", "Bolg", "Golfimbul", "Gorbag", "Gorgol", "Gothmog", "Grishnákh", "Lugdusz", "Mauhur", "Muzgash",
             "Radbug", "Szagrat", "Snaga", "Cirith", "Ungol", "Uglúk", "Uftak"]

class Player:
    def __init__(self, name, klasa):
        self.name = name
        self.name = self.name[0]
        self.klasa = klasa
        self.poziom = 1
        self.dext = 0
        self.str = 0
        self.intel = 0
        self.HP = 0
        self.MP = 0
        self.defense = 0
        self.mdefense = 0
        self.dodge = 0
        self.xpoz = random.randint(1, 10)
        self.ypoz = random.randint(1, 10)
        self.war = {'classname': 'war', 'HP': 100, 'MP': 60, 'dext': 2, 'str': 4, 'intel': 2}
        self.mag = {'classname': 'mag', 'HP': 70, 'MP': 90, 'dext': 4, 'str': 1, 'intel': 4}
        self.thi = {'classname': 'thi', 'HP': 80, 'MP': 80, 'dext': 7, 'str': 2, 'intel': 2}
        self.infoklasy = {}
        self.update()

    def update(self):
        if self.klasa == "war":
            self.infoklasy = self.war
        elif self.klasa == "mag":
            self.infoklasy = self.mag
        elif self.klasa == "thi":
            self.infoklasy = self.thi

        self.dext = self.poziom * self.infoklasy["dext"]
        self.str = self.poziom * self.infoklasy["str"]
        self.intel = self.poziom * self.infoklasy["intel"]
        self.HP = self.poziom * self.infoklasy["HP"] + self.poziom * self.infoklasy["str"]
        self.MP = self.poziom * self.infoklasy["MP"] + self.poziom * self.infoklasy["intel"]
        self.defense = self.poziom * self.infoklasy["str"] * 0.7
        self.mdefense = self.poziom * self.infoklasy["intel"] * 0.7
        self.dodge = self.poziom * self.infoklasy["dext"] * 0.7


npc_count = 3


def generator_npc(il):
    potwory = [NPC() for u in range(il)]
    return potwory

potwory = generator_npc( npc_count )
for potwor in potwory:
    print(potwor.name)
