from datetime import date
from animal import Animal


class PettingAreaAnimal(Animal):
    def __init__(self, name, species, shift, date_added=None):
        super().__init__(name, species, "Petting Area", date_added)
        self.walking = True
        self.shift = shift


class Horse(PettingAreaAnimal):
    def __init__(self, name, shift, date_added=None):
        super().__init__(name, "Horse", shift, date_added)
