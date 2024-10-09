import pytest
from classes.Burger import Burger
from classes.Pizza import Pizza
from classes.vok import Vok

def test_burger():
    bg = Burger()
    bg.calculate_energy_cost([10,15,20])
    bg.calculate_money_cost([15, 15, 30])
    assert isinstance(bg, Burger) == True
    assert bg.get_energy_cost == 45
    assert bg.get_money_cost == 60

def test_pizza():
    pz = Pizza()
    pz.calculate_energy_cost([15, 20, 25])
    pz.calculate_money_cost([20, 15, 30])
    assert isinstance(pz, Pizza) == True
    assert pz.get_energy_cost == 60
    assert pz.get_money_cost == 65

def test_vok():
    vk = Vok()
    vk.calculate_energy_cost([100, 100, 20])
    vk.calculate_money_cost([20, 50, 30])
    assert isinstance(vk, Vok) == True
    assert vk.get_energy_cost == 220
    assert vk.get_money_cost == 100
