from datetime import date
from animal import Animal


class PondAnimal(Animal):
    def __init__(self, name, species, date_added=None):
        super().__init__(name, species, "Pond", date_added)
        self.swimming = True


class GoldFish(PondAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Gold Fish", date_added)
