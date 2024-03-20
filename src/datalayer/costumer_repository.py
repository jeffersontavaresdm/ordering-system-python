from dataclasses import dataclass

from src.datalayer.base import RepositoryInterface
from src.domains.customer import CustomerRegistration, Customer


@dataclass
class CustomerRepository(RepositoryInterface):

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        raise NotImplementedError

    async def email_already_exists(self, email: str) -> bool:
        raise NotImplementedError
