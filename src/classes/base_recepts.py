from abc import ABCMeta, abstractmethod, abstractproperty

class BaseRecepts:
    energy_cost = 0.0
    money_cost = 0
    __metaclass__=ABCMeta

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Значения базового класса: энерг.ценность: {self.energy_cost}, количество: {self.money_cost}'

    @property
    def get_money_cost(self) -> int:
        return self.money_cost

    @property
    def get_energy_cost(self) -> float:
        return self.energy_cost

    @abstractmethod
    def calculate_energy_cost(self, energy_list : list) -> float:
        pass

    @abstractmethod
    def calculate_money_cost(self, money_list : list):
        pass
