class Weather:
    """базовый класс для Погоды"""

    def __init__(self, name, growth_rate):
        self.name = name
        self.growth_rate = growth_rate

    def __str__(self):
        return self.name


class Rain(Weather):
    """наследник класса Погоды"""

    def __init__(self):
        super().__init__("Дождь", 0.5)


class Sun(Weather):
    """наследник класса Погоды"""

    def __init__(self):
        super().__init__("Солнце", 1)


class Drought(Weather):
    """наследник класса Погоды"""

    def __init__(self):
        super().__init__("Засуха", 0.1)
