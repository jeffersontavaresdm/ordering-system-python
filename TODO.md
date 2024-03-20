# Ordering System

- Customer
    - name
    - email

- Product
    - name
    - description
    - price

- Order
    - [OrderStatus]
    - [OrderItem]
    - total

- OrderStatus
    - name (ACOMPLISHED, IN PREPARATION, SENT, DELIVERED, FINISHED)

- OrderItem
    - product_id
    - price
    - quantity