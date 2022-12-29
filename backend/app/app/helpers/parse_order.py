from app.order import Order


def parse_order(data_row) -> Order:
    """Converts a database row to an Order object."""
    return Order(**data_row)
