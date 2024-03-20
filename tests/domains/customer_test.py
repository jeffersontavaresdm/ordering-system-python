from src.domains.customer import Customer, Address


def test_should_create_customer():
    name = "jonh doe"
    email = "jonh@email.com"

    address: Address = Address(street="S01", neighborhood="N01", city="C01")
    customer: Customer = Customer(name=name, email=email, address=address)

    customer_model_dump = customer.model_dump()
    address_model_dump = address.model_dump()

    assert customer_model_dump is not None
    assert isinstance(customer_model_dump, dict)
    assert customer_model_dump.get("name") == name
    assert customer_model_dump.get("email") == email
    assert customer_model_dump.get("address") == address_model_dump
