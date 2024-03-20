from src.datalayer.costumer_repository import CustomerRepository
from src.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.domains.customer import Customer, CustomerRegistration


class CustomerRepositoryMock(CustomerRepository):

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        customer: Customer = Customer(**customer_registration.model_dump())

        CUSTOMER_DB.append(customer)

        return customer

    async def email_already_exists(self, email: str) -> bool:
        return len(list(filter(lambda customer: customer.email == email, CUSTOMER_DB))) >= 1
