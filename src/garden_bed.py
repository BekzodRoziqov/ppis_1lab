class GardenBed:
    """базовый класс для Сада"""

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.plots = []

    def add_plot(self, plot):
        self.plots.append(plot)
        print(f"Грядка {plot.name} создана! \n")

    def get_plots(self):
        return self.plots

    def get_plot_by_name(self, name):
        for plot in self.plots:
            if plot.name == name:
                return plot
        print('Участок с названием ' + name + ' не найден')
        return None

    def remove_plot_by_name(self, name):
        for i in range(len(self.plots)):
            if self.plots[i].name == name:
                del self.plots[i]
                return
        raise Exception('Участок с названием ' + name + ' не найден')

    def get_garden_name(self):
        return self.name
