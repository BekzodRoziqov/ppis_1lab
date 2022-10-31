from .plants import Tree, Vegetable
from .weather import Drought, Rain, Sun


class GameSimulator:
    """базовый класс для Симулятора Сада"""

    def __init__(self, garden):
        self.garden = garden
        self.weather = None

    def set_weather(self, weather):
        if weather == "1":
            self.weather = Rain()
            print("Погода сейчас дождь \n")
        elif weather == "2":
            self.weather = Sun()
            print("Погода сейчас солнце \n")
        elif weather == "3":
            print("Погода сейчас засуха \n")
            self.weather = Drought()

    def simulate(self):
      # Garden simulator with growth of plants
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                plant.grow()
                if self.weather.name == "Дождь":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Солнце":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Засуха":
                    plant.growth += self.weather.growth_rate

                if plant.is_grown():
                    print(f'{plant} вырос')

        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                if plant.is_grown():
                    print(f'{plant} собирают')
                    plant.growth = 0
                    plant.harvested = True
                    if isinstance(plant, Vegetable):
                        plot.add_plant(plant.seed)
                    elif isinstance(plant, Tree):
                        plot.add_plant(plant.seed)

        print(f"Симуляция сада {self.garden.get_garden_name()}\n")
        print(f"Проверить результат с на опции \n")

    def print_garden(self):
        for plot in self.garden.get_plots():
            print(plot)
            for plant in plot.get_plants():
                print(plant, plant.growth)
            print()

    def harvest(self):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    plot.add_plant(plant.seed)
                    plant.seed = None

    def get_plot_by_name(self, name):
        return self.garden.get_plot_by_name(name)

    def get_plant_by_name(self, name):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.name == name:
                    return plant
        return None
