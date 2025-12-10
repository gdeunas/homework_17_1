from src.product import Product


def test_print_mixin(capsys):
    """Test the print_mixin function."""
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
