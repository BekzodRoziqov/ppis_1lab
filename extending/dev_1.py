class CareRecipe:
    def __init__(self, name, watering, weeding, fertilizing, pest_control):
        self.name = name
        self.watering = watering
        self.weeding = weeding
        self.fertilizing = fertilizing
        self.pest_control = pest_control

    def is_dry_up(self):
        return self.watering == 0

    def is_watered(self):
        return self.watering

    def is_weeded(self):
        return self.weeding

    def is_fertilized(self):
        return self.fertilizing

    def __str__(self):
        return self.name
