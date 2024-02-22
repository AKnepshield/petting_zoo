from datetime import date
from animal import Animal


class PettingAreaAnimal(Animal):
    def __init__(self, name, species, shift, food, date_added=None):
        super().__init__(name, species, "Petting Area", date_added)
        self.swimming = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")


class Rat(PettingAreaAnimal):
    def __init__(self, name, shift, date_added=None):
        super().__init__(name, "Rat", shift, date_added)
