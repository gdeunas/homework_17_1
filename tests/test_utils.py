import json
from json import JSONDecodeError
from unittest.mock import mock_open, patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


@pytest.fixture
def some_data():
    return read_json("../data/products.json")


def test_create_objects(some_data):
    categories = create_objects_from_json(some_data)
    assert isinstance(categories, list)
    assert all(isinstance(c, Category) for c in categories)
    assert all(isinstance(p, Product) for c in categories for p in c.products)


def test_read_json_success(tmp_path):
    file_path = tmp_path / "test.json"
    sample_data = [{"name": "cat1", "products": []}]
    file_path.write_text(json.dumps(sample_data), encoding="utf-8")

    result = read_json(str(file_path))
    assert result == sample_data


def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json("non_existent.json")
        assert result == []


def test_read_json_decode_error():
    m_open = mock_open(read_data="invalid json")
    with patch("builtins.open", m_open):
        with patch(
            "json.load", side_effect=JSONDecodeError("Expecting value", "doc", 0)
        ):
            result = read_json("dummy.json")
            assert result == []
