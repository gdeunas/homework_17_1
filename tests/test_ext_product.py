import pytest


def test_ext_product_smartphone(ext_product_smartphone1):
    assert ext_product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert ext_product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert ext_product_smartphone1.price == 180000.0
    assert ext_product_smartphone1.quantity == 5
    assert ext_product_smartphone1.efficiency == 95.5
    assert ext_product_smartphone1.model == "S23 Ultra"
    assert ext_product_smartphone1.memory == 256
    assert ext_product_smartphone1.color == "Серый"


def test_ext_product_smartphone_add(ext_product_smartphone1, ext_product_smartphone2):
    assert ext_product_smartphone1 + ext_product_smartphone2 == 13.0


def test_ext_product_smartphone_add1(ext_product_smartphone1, ext_product_smartphone2):
    with pytest.raises(TypeError):
        print(ext_product_smartphone1 + 1)


def test_ext_product_grass(ext_product_grass1):
    assert ext_product_grass1.name == "Газонная трава"
    assert ext_product_grass1.description == "Элитная трава для газона"
    assert ext_product_grass1.price == 500.0
    assert ext_product_grass1.quantity == 20
    assert ext_product_grass1.country == "Россия"
    assert ext_product_grass1.germination_period == "7 дней"
    assert ext_product_grass1.color == "Зеленый"


def test_ext_product_grass_add(ext_product_grass1, ext_product_grass2):
    assert ext_product_grass1 + ext_product_grass2 == 35.0


def test_ext_product_grass_add1(ext_product_grass1, ext_product_grass2):
    with pytest.raises(TypeError):
        print(ext_product_grass1 + 1)
