import pytest

from src.category import Order
from src.product import Product


def test_category_init(first_category, second_category):
    """test category class"""
    assert first_category.name == "category_n"
    assert first_category.description == "category_dec"
    assert len(first_category.product_in_list) == 2
    assert len(second_category.product_in_list) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.all_products_count == 3


def test_category_products_property(first_category):
    assert (
        first_category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_products_setter(
    first_category, product, product_with1, product_with2
):
    assert len(first_category.product_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.product_in_list) == 3


def test_category_str(first_category):
    assert str(first_category) == "category_n, количество продуктов: 22 шт."


def test_category_products_setter_error(
    first_category, product, product_with1, product_with2
):
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_category_product_setter_smartphone(first_category, ext_product_smartphone1):
    first_category.add_product(ext_product_smartphone1)
    assert first_category.product_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_order_str_method():
    product = Product("Prod10", "Desc10", 100.0, 5)
    order = Order(product, 3)
    expected_str = f"Заказ на товар: {product.name}, количество: 3, итоговая стоимость: {product.price * 3} руб."
    assert str(order) == expected_str


def test_category_product_middle_price(first_category):
    assert first_category.middle_price() == 120500.0


def test_category_no_product_middle_price(third_category):
    assert third_category.middle_price() == 0
