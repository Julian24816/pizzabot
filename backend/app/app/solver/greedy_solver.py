from typing import List

from app.order import Order
from app.solver.pizza import Pizza
from app.solver.pizza_variant import variants
from app.solver.solver import Solver


class GreedySolver(Solver):
    def __init__(self, pieces_per_pizza: int = 12):
        self.pieces_per_pizza = pieces_per_pizza

    def solve(self, orders: List[Order]) -> List[Pizza]:
        pizzas: List[Pizza] = []
        for variant in reversed(variants):
            for order in orders:
                pieces = order.number_of_pieces[variant]
                for _ in range(pieces):
                    if not pizzas or pizzas[-1].is_full():
                        # pizza creation needed
                        pizzas.append(Pizza(variant, self.pieces_per_pizza))
                    pizzas[-1].add_order(order)
        return pizzas
