from datetime import date


class Animal:
    def __init__(self, name, species, location, date_added=None):
        self.name = name
        self.species = species
        self.location = location
        self.date_added = date.today()

    def __str__(self):
        attributes = vars(self)
        output = ""

        for key, value in attributes.items():
            output += f"{key}: {value}\n"
        return output.strip()
