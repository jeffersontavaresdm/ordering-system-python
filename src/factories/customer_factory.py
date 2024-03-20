from src.datalayer.costumer_repository import CustomerRepository
from src.datalayer.repositories.mock.customer_repository_mock import CustomerRepositoryMock
from src.services.base import ServiceBase
from src.services.customer_service import CustomerService


class CustomerFactory:

    @staticmethod
    def create_mock():
        repository: CustomerRepository = CustomerRepositoryMock()
        service: ServiceBase = CustomerService(repository=repository)
        return service
