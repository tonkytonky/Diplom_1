import pytest
from assertpy import assert_that

from praktikum import Burger


class TestBurger:
    def test_create_buns(self, bun, ingredients):
        ingredients = ingredients(number=3)

        burger = Burger()
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient.ingredient)

        description = "Ингредиент создан неверно"
        assert_that(burger, description=description).is_type_of(Burger)