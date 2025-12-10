import pytest

from src.category import Category
from src.ext_product import LawnGrass, Smartphone
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_category():
    return Category(
        name="category_n",
        description="category_dec",
        products=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="category_n2",
        description="category_dec2",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
        ],
    )


@pytest.fixture
def third_category():
    return Category(
        name="category_n3",
        description="category_desc3",
        products=[],
    )


@pytest.fixture
def product():
    return Product(
        name="product_n",
        description="product_dec",
        price=12.2,
        quantity=10,
    )


@pytest.fixture
def product_with1():
    return Product(
        name="product_n1", description="product_desc", price=12.1, quantity=11
    )


@pytest.fixture
def product_with2():
    return Product(
        name="product_n2", description="product_desc", price=12.2, quantity=12
    )


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)


@pytest.fixture
def ext_product_smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def ext_product_smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def ext_product_grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def ext_product_grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
