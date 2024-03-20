from typing import Optional

from pydantic import BaseModel

from src.domains.BaseDomain import BaseDomain


class Address(BaseDomain):
    street: str
    neighborhood: str
    city: str


class Customer(BaseDomain):
    name: str
    email: str
    address: Optional[Address] = None


class CustomerRegistration(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str
