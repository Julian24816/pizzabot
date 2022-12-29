from dataclasses import dataclass, field


@dataclass
class PizzaVariant:
    name: str
    pieces_per_pizza: int = 12


@dataclass
class Event:
    id: int | None = None
    title: str | None = None
    descr: str | None = None
    pizza_variants: list[PizzaVariant] = field(
        default_factory=lambda: [PizzaVariant("meat"), PizzaVariant("vegetarian"), PizzaVariant("vegan")])
    new_orders_allowed: bool = True
    editing_orders_allowed: bool = True
