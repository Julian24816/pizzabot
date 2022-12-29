from dataclasses import dataclass


class OrderValidException(Exception):
    pass


@dataclass
class Order:
    user_name: str
    number_of_meat_pieces: int
    number_of_vegetarian_pieces: int
    number_of_vegan_pieces: int
    id: int | None = None

    def check_validity(self):
        if self.user_name.strip() == "":
            raise OrderValidException("Name is missing!")
        if self.number_of_meat_pieces < 0:
            raise OrderValidException("Number of meat pieces is negative!")
        if self.number_of_vegetarian_pieces < 0:
            raise OrderValidException("Number of vegetarian pieces is negative!")
        if self.number_of_vegan_pieces < 0:
            raise OrderValidException("Number of vegan pieces is negative!")
        if self.number_of_meat_pieces + self.number_of_vegetarian_pieces + self.number_of_vegan_pieces < 1:
            raise OrderValidException("No pizza pieces selected!")

    def __iter__(self):
        yield "user_name", self.user_name
        yield "number_of_meat_pieces", self.number_of_meat_pieces
        yield "number_of_vegetarian_pieces", self.number_of_vegetarian_pieces
        yield "number_of_vegan_pieces", self.number_of_vegan_pieces
        yield "id", self.id
