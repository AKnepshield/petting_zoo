from datetime import date
from animal import Animal


class GlassTankAnimal(Animal):
    def __init__(self, name, species, date_added=None):
        super().__init__(name, species, "Glass Tank", date_added)
        self.slithering = True


class Gecko(GlassTankAnimal):
    def __init__(self, name, date_added=None):
        super().__init__(name, "Gecko", date_added)
