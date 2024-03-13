from src.domain.order import Order, OrderStatus, OrderItem, OrderStatusName


def test_status_name_should_init_defaut_value():
    order_status = OrderStatus()
    assert order_status.name == OrderStatusName.ACCOMPLISHED


def test_should_create_order():
    order_status = OrderStatus()

    status_model_dump = order_status.model_dump()

    assert status_model_dump is not None
    assert isinstance(status_model_dump, dict)
    assert status_model_dump.get("name") == OrderStatusName.ACCOMPLISHED

    product_id = 1
    price = 1
    quantity = 1
    order_item = OrderItem(product_id=product_id, price=price, quantity=quantity)
    item_model_dump = order_item.model_dump()

    assert item_model_dump is not None
    assert isinstance(item_model_dump, dict)
    assert item_model_dump.get("product_id") == product_id
    assert item_model_dump.get("price") == price
    assert item_model_dump.get("quantity") == quantity

    order: Order = Order()

    assert order.status == []
    assert order.items == []

    order.add_status(order_status)
    order.add_item(order_item)

    order_model_dump = order.model_dump()

    assert order_model_dump is not None
    assert isinstance(order_model_dump, dict)
    assert order_model_dump.get("status") == [status_model_dump]
    assert order_model_dump.get("items") == [item_model_dump]
