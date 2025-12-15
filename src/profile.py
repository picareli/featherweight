# from collections import namedtuple

class Profile:
    def __init__(self, height: float, target_weight: float, target_date: float):
        self.height = height
        self.target_weight = target_weight
        self.target_date = target_date
        self.bmi = None
        self.max_weight = None
        self.min_weight = None

    def calculate_bmi (self, height: float, weight: float):
        return height / (weight ** 2)