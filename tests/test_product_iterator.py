import pytest


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == '55" QLED 4K'
    with pytest.raises(StopIteration):
        next(product_iterator)
