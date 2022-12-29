from dataclasses import dataclass
from typing import List

from app.order import Order


@dataclass
class Pizza:
    def __init__(self, variant: str, pieces: int):
        self.variant = variant
        self.pieces = pieces
        self.assigned_orders: List[Order] = []

    def add_order(self, order: Order):
        if self.is_full():
            raise Exception("Pizza is full!")
        self.assigned_orders.append(order)

    def is_full(self):
        return self.pieces == len(self.assigned_orders)

    def __iter__(self):
        yield "variant", self.variant
        yield "pieces", self.pieces
        yield "assigned_orders", self.assigned_orders
