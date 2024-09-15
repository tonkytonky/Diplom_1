from random import randint

import pytest
from assertpy import assert_that

from praktikum import Ingredient
from praktikum import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from utils import generate_random_string


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
        ]
    )
    def test_create_ingredient(self, ingredient_type):
        ingredient = Ingredient(
            ingredient_type=ingredient_type,
            name=generate_random_string(10),
            price=randint(100, 500),
        )
        description = "Ингредиент создан неверно"
        assert_that(ingredient, description=description).is_type_of(Ingredient)
        description = f'Метод "get_type" Ингредиента вернул неверные данные'
        assert_that(ingredient.get_type(), description=description).is_equal_to(ingredient_type)

    @pytest.mark.parametrize(
        "getter_method, expected_result", [
            ("get_name", "name"),
            ("get_price", "price"),
        ]
    )
    def test_getters(self, ingredients, getter_method, expected_result):
        ingredient = ingredients(number=1)[0]

        expected_result = getattr(ingredient.ingredient_data, expected_result)
        getter_method = getattr(ingredient.ingredient, getter_method)
        actual_result = getter_method()

        description = f'Метод "{getter_method}" Ингредиента вернул неверные данные'
        assert_that(expected_result, description=description).is_equal_to(actual_result)
