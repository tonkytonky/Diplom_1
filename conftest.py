from random import choice as random_choice

import pytest

from data import BunData, IngredientData
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    bun = Bun(name=BunData.name, price=BunData.price)
    return bun


@pytest.fixture
def ingredient():
    ingredient_type = random_choice((
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ))
    ingredient = Ingredient(
        ingredient_type=ingredient_type,
        name=IngredientData.name,
        price=IngredientData.price,
    )
    return ingredient
