from datetime import date
from animal import Animal


class PettingAreaAnimal(Animal):
    def __init__(self, name, species, date_added=None):
        super().__init__(name, species, "Petting Area", date_added)
        self.walking = True


class Horse(PettingAreaAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Horse", date_added)
