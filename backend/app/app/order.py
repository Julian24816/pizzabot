from dataclasses import dataclass
from typing import Dict
from app.solver.pizza_variant import variants


class OrderValidException(Exception):
    pass


@dataclass
class Order:
    user_name: str
    number_of_pieces: Dict[str, int]
    id: int | None = None

    def check_validity(self):
        if self.user_name.strip() == "":
            raise OrderValidException("Name is missing!")
        for variant, pieces in self.number_of_pieces.items():
            if pieces < 0:
                raise OrderValidException(f"Invalid number of pieces for {variant}!")
            if variant not in variants:
                raise OrderValidException(f"unknown variant: {variant}")
        if sum(self.number_of_pieces.values()) == 0:
            raise OrderValidException("No pieces ordered!")

    def __iter__(self):
        yield "user_name", self.user_name
        yield "number_of_pieces", self.number_of_pieces
        yield "id", self.id
