import pytest

from src.product import Product


def test_product_init(product):
    """test product class"""
    assert product.name == "product_n"
    assert product.description == "product_dec"
    assert product.price == 12.2
    assert product.quantity == 10


def test_product_new_product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_product_price(capsys, product):
    product.price = -5
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-1]
        == "Цена не должна быть нулевая или отрицательная"
    )


def test_product_str(product):
    assert str(product) == "product_n, 12.2 руб. Остаток: 10 шт."


def test_product_add(product_with1, product_with2):
    assert product_with1 + product_with2 == 279.5


def test_product():
    with pytest.raises(ValueError) as exc_info:
        Product(name="product_n3", description="product_desc3", price=12.1, quantity=0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
