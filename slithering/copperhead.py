from datetime import date
from animal import Animal


class GlassTankAnimal(Animal):
    def __init__(self, name, species, food, date_added=None):
        super().__init__(name, species, "Glass Tank", date_added)
        self.slithering = True
        self.food = food
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")


class CopperheadSnake(GlassTankAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Copperhead Snake", date_added)
