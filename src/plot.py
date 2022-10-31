class Plot:
    """базовый класс для Грядки"""

    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def get_plants(self):
        return self.plants

    def get_plant(self, index):
        return self.plants[index]

    def get_plant_by_name(self, name):
        for plant in self.plants:
            if plant.name == name:
                return plant
        return None
