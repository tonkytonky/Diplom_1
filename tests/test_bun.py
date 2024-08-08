import pytest
from assertpy import assert_that

from data import BunData
from praktikum.bun import Bun


class TestBun:
    def test_create_bun(self):
        bun = Bun(name=BunData.name, price=BunData.price)
        description = "Булочка создана неверно"
        assert_that(bun, description=description).is_type_of(Bun)

    @pytest.mark.parametrize(
        "method_name, expected_result", [
            ("get_name", BunData.name),
            ("get_price", BunData.price),
        ]
    )
    def test_getters(self, bun, method_name, expected_result):
        actual_result = getattr(bun, method_name)()
        description = f'Метод "{method_name}" Булочки вернул неверные данные'
        assert_that(expected_result, description=description).is_equal_to(actual_result)
