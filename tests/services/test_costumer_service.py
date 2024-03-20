import pytest

from src.domains.customer import CustomerRegistration
from src.exceptions.customer_exceptions import EmailAlreadyExistsException
from src.factories.customer_factory import CustomerFactory


@pytest.mark.asyncio
async def test_should_create_customer():
    service = CustomerFactory.create_mock()
    customer = CustomerRegistration(
        name="Jonh Doe",
        email="jonh@gmail.com",
        password="123123",
        confirm_password="123123",
    )

    response = await service.register(customer_registration=customer)

    print(f"\nTEST:", response)


@pytest.mark.asyncio
async def test_should_throws_email_already_exists_exception():
    service = CustomerFactory.create_mock()
    customer = CustomerRegistration(
        name="Jonh Doe",
        email="jonh@gmail.com",
        password="123123",
        confirm_password="123123",
    )

    with pytest.raises(EmailAlreadyExistsException) as error:
        await service.register(customer_registration=customer)
    assert str(error.value) == f"Email '{customer.email}' already exists"
