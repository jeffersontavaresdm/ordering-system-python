from src.domains.customer import Customer, Address
from src.domains.order import Order, OrderStatus, OrderItem, OrderStatusName

product_id = 1
price = 1
quantity = 1

address: Address = Address(street="S01", neighborhood="N01", city="C01")
customer: Customer = Customer(name="jonh doe", email="jonh@email.com", address=address)


def test_status_name_should_init_defaut_value():
    order_status = OrderStatus()
    assert order_status.name == OrderStatusName.ACCOMPLISHED


def test_order_status():
    order_status = OrderStatus()
    status_model_dump = order_status.model_dump()

    assert status_model_dump is not None
    assert isinstance(status_model_dump, dict)
    assert status_model_dump.get("name") == OrderStatusName.ACCOMPLISHED


def test_order_item():
    order_item = OrderItem(product_id=product_id, price=price, quantity=quantity)
    item_model_dump = order_item.model_dump()

    assert item_model_dump is not None
    assert isinstance(item_model_dump, dict)
    assert item_model_dump.get("product_id") == product_id
    assert item_model_dump.get("price") == price
    assert item_model_dump.get("quantity") == quantity


def test_order_creation():
    order: Order = Order(customer=customer)

    assert order.status == []
    assert order.items == []


def test_add_status_to_order():
    order = Order(customer=customer)
    order_status = OrderStatus()

    order.add_status(order_status)

    order_model_dump = order.model_dump()

    status_model_dump = order_status.model_dump()

    assert order_model_dump is not None
    assert isinstance(order_model_dump, dict)
    assert order_model_dump.get("status") == [status_model_dump]


def test_add_item_to_order():
    order = Order(customer=customer)

    order_item = OrderItem(product_id=product_id, price=price, quantity=quantity)

    order.add_item(order_item)

    order_model_dump = order.model_dump()

    item_model_dump = order_item.model_dump()

    assert order_model_dump is not None
    assert isinstance(order_model_dump, dict)
    assert order_model_dump.get("items") == [item_model_dump]


def test_order_total_value():
    price1 = 5000
    price2 = 2000
    price3 = 3000
    quantity1 = 2
    quantoty2 = 1
    quantity3 = 1
    total = (price1 * quantity1) + (price2 * quantoty2) + (price3 * quantity3)

    order_item1 = OrderItem(product_id=1, price=price1, quantity=quantity1)
    order_item2 = OrderItem(product_id=2, price=price2, quantity=quantoty2)
    order_item3 = OrderItem(product_id=3, price=price3, quantity=quantity3)

    order = Order(customer=customer)
    order.add_item(order_item1)
    order.add_item(order_item2)
    order.add_item(order_item3)

    order_total = order.total()

    print("\nTOTAL: " + str(order_total))

    assert order_total == total
