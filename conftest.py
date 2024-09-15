from random import choice as random_choice
from random import randint

import pytest

from data import BunData
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from utils import generate_random_string


class IngredientData:
    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price


class IngredientWrapper:
    def __init__(self, ingredient_data: IngredientData):
        self.ingredient_data = ingredient_data
        self.ingredient = Ingredient(
            ingredient_type=ingredient_data.type_,
            name=ingredient_data.name,
            price=ingredient_data.price,
        )


@pytest.fixture
def bun():
    bun = Bun(name=BunData.name, price=BunData.price)
    return bun


@pytest.fixture
def ingredients():
    def ingredient_fabric(number):
        ingredients = []
        for _ in range(number):
            ingredient = IngredientWrapper(
                ingredient_data=IngredientData(
                    type_=random_choice((
                        INGREDIENT_TYPE_SAUCE,
                        INGREDIENT_TYPE_FILLING,
                    )),
                    name=generate_random_string(10),
                    price=randint(100, 500),
                )
            )
            ingredients.append(ingredient)
        return ingredients

    return ingredient_fabric
