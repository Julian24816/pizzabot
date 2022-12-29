import dataset
from app.helpers.parse_order import parse_order
from app.solver.greedy_solver import GreedySolver
from flask import Flask, request, jsonify
from flask_cors import *
from sqlalchemy.exc import IntegrityError
from .order import Order, OrderValidException

app = Flask(
    __name__,
    static_folder="../../../frontend/public",
    static_url_path="/static",
)
CORS(app)
db = dataset.connect(
    'sqlite:///db.sqlite', engine_kwargs={"connect_args": {'check_same_thread': False}})
orders = db["orders"]
orders.create_column('user_name', db.types.string, unique=True, nullable=False)


@app.route("/order", methods=["POST"])
def add_order():
    try:
        order = Order(**request.json)
    except TypeError:
        return jsonify({"error": "Invalid order"}), 400
    try:
        order.check_validity()
    except OrderValidException as e:
        return jsonify({"error": e.message_key, "variant": e.variant}), 400
    order_dict = dict(order)
    del order_dict["id"]
    try:
        order.id = orders.insert(order_dict)
    except IntegrityError as e:
        return jsonify({"error": "userExists"}), 400
    return jsonify(order)


@app.route("/order/<int:id>", methods=["DELETE"])
def delete_order(id: int):
    orders.delete(id=id)
    return "", 204


def get_all_orders() -> list[Order]:
    return [parse_order(order) for order in orders]


@app.route("/order")
def get_orders():
    return jsonify(get_all_orders())


@app.route("/solved")
def solved():
    solver = GreedySolver()
    pizzas = solver.solve(get_all_orders())
    return jsonify([dict(pizza) for pizza in pizzas])


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/<path:path>")
def serve(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5113,
        debug=True,
        use_reloader=True,
    )
