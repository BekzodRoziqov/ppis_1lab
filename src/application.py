from .game_simulator import GameSimulator
from .garden_bed import GardenBed
from .plants import Tree, Vegetable
from .plot import Plot


class GardenSimulatorApp:
    """класс реализующие поведение класса Симулятора Сада"""

    def __init__(self):
        self.garden = self.set_garden()
        self.simulator = GameSimulator(self.garden)
        self.weather = None

    def set_garden(self):
        name = input('Введите имя сада: ')
        size = int(input('Введите размер сада: '))
        return GardenBed(name, size)

    def create_plot(self):
        name = input("Введите название участка:")
        plot = Plot(name)
        self.garden.add_plot(plot)

    def create_plant(self, choice, name, growth_rate, growth_time,
                     harvest_time, seed_rate, dig_time=0, treat_time=0):

        if choice == '1':
            plant = Tree(name, growth_rate, growth_time,
                         harvest_time, seed_rate, dig_time)
        elif choice == '2':
            plant = Vegetable(name, growth_rate, growth_time,
                              harvest_time, seed_rate, treat_time)

        plot_name = input("Введите название участка: ")
        plot = self.simulator.get_plot_by_name(plot_name)

        if plant and plot:
            plot.add_plant(plant)
            print("Растение добавлено на участок \n")

    def set_weather(self, weather):
        self.simulator.set_weather(weather)

    def simulate(self):
        self.simulator.simulate()

    def print_garden(self):
        self.simulator.print_garden()

    def get_plant(self):
        name = input("Введите название растения: ")
        plant = self.simulator.get_plant_by_name(name)
        print(plant)

    def get_plot(self):
        name = input("Введите название участка: ")
        plot = self.simulator.get_plot_by_name(name)
        print(plot)
