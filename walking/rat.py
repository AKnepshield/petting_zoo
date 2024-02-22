from datetime import date
from animal import Animal


class PettingAreaAnimal(Animal):
    def __init__(self, name, species, date_added=None):
        super().__init__(name, species, "Petting Area", date_added)
        self.swimming = True


class Rat(PettingAreaAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Rat", date_added)
