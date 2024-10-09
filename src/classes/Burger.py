import math
from base_recepts import BaseRecepts

class Burger(BaseRecepts):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f'Значения класса Burger: энерг.цен.: {self.energy_cost}, стоимость: {self.money_cost}'

    def calculate_energy_cost(self, energy_list: list):
        self.energy_cost = sum(energy_list)

    def calculate_money_cost(self, money_list: list):
        self.money_cost = sum(money_list)
