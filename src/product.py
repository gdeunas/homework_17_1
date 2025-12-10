from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        sum_of_products: float = 0,
    ):
        """Для класса Product определите следующие свойства:
        название (name),
        описание (description),
        цена (price),
        количество в наличии (quantity)."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.sum_of_products = sum_of_products
        super().__init__()

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить {type(self)} с {type(other)}")

        if type(self) is Product and type(other) is Product:
            return float(self.price * self.quantity + other.price * other.quantity)

        if type(self) is type(other):
            return self.quantity + other.quantity

        raise TypeError(f"Нельзя сложить {type(self)} с {type(other)}")

    @classmethod
    def new_product(cls, product):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
