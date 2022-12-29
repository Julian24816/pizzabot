from dataclasses import dataclass


@dataclass
class Order:
    user_name: str
    number_of_meat_pieces: int
    number_of_vegetarian_pieces: int
    number_of_vegan_pieces: int
    id: int | None = None

    def __iter__(self):
        yield "user_name", self.user_name
        yield "number_of_meat_pieces", self.number_of_meat_pieces
        yield "number_of_vegetarian_pieces", self.number_of_vegetarian_pieces
        yield "number_of_vegan_pieces", self.number_of_vegan_pieces
        yield "id", self.id
