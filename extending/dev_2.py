class Diseases:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def is_diseased(self):
        return self.damage >= 100

    def diseases(self):
        self.damage += 10

    def __str__(self):
        return f'Diseases {self.name} has damage {self.damage}'

    def __repr__(self):
        return f'Diseases {self.name} has damage {self.damage}'
