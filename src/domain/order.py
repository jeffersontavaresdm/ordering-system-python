from enum import Enum

from pydantic import Field

from src.domain.BaseDomain import BaseDomain


class OrderStatusName(str, Enum):
    ACCOMPLISHED = "ACCOMPLISHED",
    IN_PREPARATION = "IN_PREPARATION",
    SENT = "SENT",
    DELIVERED = "DELIVERED",
    FINISHED = "FINISHED"


class OrderStatus(BaseDomain):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED)


class OrderItem(BaseDomain):
    product_id: int
    price: float
    quantity: int


class Order(BaseDomain):
    status: list[OrderStatus] = Field(default=[])
    items: list[OrderItem] = Field(default=[])

    def add_status(self, status: OrderStatus):
        self.status.append(status)

    def add_item(self, item: OrderItem):
        self.items.append(item)
