from typing import Union

from src.base_product import BaseOrder
from src.product import Product


class Category(BaseOrder):
    category_count = 0
    product_count = 0
    all_products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Для класса Category определите следующие свойства:
        название (name),
        описание (description),
        список товаров категории (products)."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.all_products_count += len(products) if products else 0

    def add_product(self, product: Union[Product | str]):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_in_list(self):
        return self.__products

    def __str__(self):
        quantity_count = 0
        for product in self.__products:
            quantity_count += product.quantity
        return f"{self.name}, количество продуктов: {quantity_count} шт."


class Order(BaseOrder):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_cost = self.product.price * self.quantity

    def __str__(self):
        return (
            f"Заказ на товар: {self.product.name}, количество: {self.quantity}, "
            f"итоговая стоимость: {self.total_cost} руб."
        )


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    print("q=", str(category1))
