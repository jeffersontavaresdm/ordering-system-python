from pydantic import BaseModel

from src.domain.BaseDomain import BaseDomain


class Customer(BaseDomain):
    name: str
    email: str
