from datetime import date
from animal import Animal


class PondAnimal(Animal):
    def __init__(self, name, species, food, date_added=None):
        super().__init__(name, species, "Pond", date_added)
        self.swimming = True
        self.food = food
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")

class GoldFish(PondAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Gold Fish", "Goldfish Chow", date_added)
    def __str__:
