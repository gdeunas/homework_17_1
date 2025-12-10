import json
from json import JSONDecodeError

from src.category import Category
from src.product import Product


def read_json(path: str) -> list:
    """Function reads json data from filepath"""
    data = []
    try:
        if path:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            return data
    except FileNotFoundError:
        print("File .env not found. Check the path.")
    except JSONDecodeError:
        print("JSONDecodeError JSON from requests.")
    return data


def create_objects_from_json(data):
    """create object from json"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories_data = create_objects_from_json(raw_data)
    print(categories_data[0].name)
    print(categories_data[0].products)
