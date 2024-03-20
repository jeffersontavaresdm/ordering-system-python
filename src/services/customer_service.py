from dataclasses import dataclass

from src.datalayer.costumer_repository import CustomerRepository
from src.domains.customer import CustomerRegistration, Customer
from src.exceptions.customer_exceptions import EmailAlreadyExistsException
from src.services.base import ServiceBase


@dataclass
class CustomerService(ServiceBase):
    repository: CustomerRepository

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        if await self.repository.email_already_exists(customer_registration.email):
            raise EmailAlreadyExistsException(message=f"Email '{customer_registration.email}' already exists")

        return await self.repository.register(customer_registration)

    async def email_already_exists(self, email: str) -> bool:
        return await self.repository.email_already_exists(email)
