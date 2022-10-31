class Plants:
    """базовый класс для Растения"""

    def __init__(self, name, growth_rate, growth_time, harvest_time):
        self.name = name
        self.growth_rate = growth_rate
        self.growth_time = growth_time
        self.harvest_time = harvest_time
        self.growth = 0

    def grow(self):
        self.growth += self.growth_rate

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time


class Seed(Plants):
    """Наследованные от Растения класс для Семян"""

    def __init__(self, plant):
        self.plant = plant

    def __str__(self):
        return self.plant.name + " семя"


class Vegetable(Plants):
    """Наследованные от Базового класса Растения класс для Овощ"""

    def __init__(self, name, growth_rate, growth_time, harvest_time, seed_rate, treat_time):
        super().__init__(name, growth_rate, growth_time, harvest_time)
        self.seed_rate = seed_rate

    def grow(self):
        super().grow()
        if self.is_grown():
            self.seed = Seed(self)

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time


class Tree(Plants):
    """Наследованные от Базового класса Растения класс для Деревьев"""

    def __init__(self, name, growth_rate, growth_time, harvest_time, seed_rate, dig_time):
        super().__init__(name, growth_rate, growth_time, harvest_time)
        self.seed_rate = seed_rate
        self.dig_time = dig_time

    def grow(self):
        super().grow()
        if self.is_grown():
            self.seed = Seed(self)

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time
