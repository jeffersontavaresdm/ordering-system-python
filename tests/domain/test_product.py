from src.domain.product import Product


def test_should_create_product():
    name = "PS5"
    description = "a very expensive video game"
    price = 5000

    product: Product = Product(name=name, description=description, price=price)

    product_model_dump = product.model_dump()

    assert product_model_dump is not None
    assert isinstance(product_model_dump, dict)
    assert product_model_dump.get("name") == name
    assert product_model_dump.get("description") == description
    assert product_model_dump.get("price") == price
