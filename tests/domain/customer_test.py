from src.domain.customer import Customer


def test_should_create_customer():
    name = "jonh doe"
    email = "jonh@email.com"

    customer: Customer = Customer(name=name, email=email)

    customer_model_dump = customer.model_dump()

    assert customer_model_dump is not None
    assert isinstance(customer_model_dump, dict)
    assert customer_model_dump.get("name") == name
    assert customer_model_dump.get("email") == email
