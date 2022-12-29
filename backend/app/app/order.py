import secrets
from dataclasses import dataclass
from typing import Dict

from app.solver.pizza_variant import variants


class OrderValidException(Exception):
    def __init__(self, message_key: str, variant: str = None):
        self.message_key = message_key
        self.variant = variant


@dataclass
class Order:
    user_name: str
    number_of_pieces: Dict[str, int]
    edit_key: str = None
    id: int | None = None

    def __post_init__(self):
        self.check_validity()
        if self.edit_key is None:
            self.generate_edit_key()

    def check_validity(self):
        if self.user_name.strip() == "":
            raise OrderValidException("missingName")
        for variant, pieces in self.number_of_pieces.items():
            if pieces < 0:
                raise OrderValidException("invalidPieceNumber", variant)
            if variant not in variants:
                raise OrderValidException("unknownVariant", variant)
        if sum(self.number_of_pieces.values()) == 0:
            raise OrderValidException("nothingOrdered")

    def generate_edit_key(self):
        self.edit_key = secrets.token_urlsafe(16)

    def __iter__(self):
        yield "user_name", self.user_name
        yield "number_of_pieces", self.number_of_pieces
        yield "edit_key", self.edit_key
        yield "id", self.id
