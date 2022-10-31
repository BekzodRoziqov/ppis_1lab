class Pests:
    """базовый класс для Вредителей"""

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'Вредители {self.name} имеет повреждение {self.damage}'
