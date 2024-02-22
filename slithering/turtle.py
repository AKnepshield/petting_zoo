from datetime import date
from animal import Animal


class PondAnimal(Animal):
    def __init__(self, name, species, food, date_added=None):
        super().__init__(name, species, "Pond", date_added)
        self.walking = True
        self.food = food
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")
    def __str__(self):
        return f"{self.name} is a {self.species}"
        
class Turtle(PondAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Turtle", date_added)
