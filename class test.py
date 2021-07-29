class Gun():
    def __init__(self):
        self.reload()

    def fire(self):
        self.ammo_count -=1

    def reload(self):
        self.ammo_count = 10



class Transformer():
    step = 1
    def __init__(self,x,Left_gun, Right_gun):
        self.Left_gun = Left_gun
        self.Right_gun = Right_gun
        self.x = x

    def run(self):
        self.x += self.step
        return self.x

    def fire(self):
        if self.Left_gun.ammo_count != 0:
            self.Left_gun.fire()
            self.Right_gun.fire()
            return self.Left_gun.ammo_count,\
               self.Right_gun.ammo_count
        else:
            self.Left_gun.reload()
            self.Right_gun.reload()
            return "Перезарядка"

class Autobot(Transformer):
    bot = "Бот"
    def transform(self):
        if self.bot == "Бот":
            self.bot = "Тачка"
            self.step = 3
        else:
            self.bot = "Бот"
            self.step = 1
        return self.bot

    def enemys(self):
        return "десептиконы"


class Deseptikon(Transformer):
    bot = 'Бот'
    def transform(self):
        if self.bot == "Бот":
            self.bot = "Смаолет"
        else:
            self.bot = "Бот"
        return self.bot


    def enemys(self):
        return "автоботы"

#Hello
#Hello
gun1 = Gun()
gun2 = Gun()
Oleg = Autobot(0,gun1,gun2)
for i in range(100):
    Patron = Oleg.fire()
    print("Олег на {0}, {2}"
          "у него {1} патрон в пушках\n"
          "{3} - его враги, "
          "Олег превращается в {4}".format(Oleg.run(),Patron,
        "Олег стреляет," if Patron!="Перезарядка" else "",
        Oleg.enemys(), Oleg.transform()))

