from datetime import datetime

import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("amount", Integer, nullable=False),
)


roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)



users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("balance", Float, nullable=False),
    Column("last_online", TIMESTAMP, default=datetime.utcnow)
)

delivery_statuses = Table(
    "delivery_statuses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("datetime_created", TIMESTAMP, default=datetime.utcnow),
    Column("datetime_changed", TIMESTAMP, default=datetime.utcnow),
    Column("delivery_status_id", Integer, ForeignKey("delivery_statuses.id"))
)

products_orders = Table(
    "products_orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("product_in_order_amount", Integer, nullable=False)
)
