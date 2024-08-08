import pytest
from assertpy import assert_that

from data import IngredientData
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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
            name=IngredientData.name,
            price=IngredientData.price,
        )
        description = "Ингредиент создан неверно"
        assert_that(ingredient, description=description).is_type_of(Ingredient)
        description = f'Метод "get_type" Ингредиента вернул неверные данные'
        assert_that(ingredient.get_type(), description=description).is_equal_to(ingredient_type)

    @pytest.mark.parametrize(
        "method_name, expected_result", [
            ("get_name", IngredientData.name),
            ("get_price", IngredientData.price),
        ]
    )
    def test_getters(self, ingredient, method_name, expected_result):
        actual_result = getattr(ingredient, method_name)()
        description = f'Метод "{method_name}" Ингредиента вернул неверные данные'
        assert_that(expected_result, description=description).is_equal_to(actual_result)
