from abc import ABCMeta
from typing import List

from app.order import Order
from app.solver.pizza import Pizza


class Solver(metaclass=ABCMeta):
    def solve(self, orders: List[Order]) -> List[Pizza]:
        ...
