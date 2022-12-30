from typing import List

import dataset
from flask import Flask, request, jsonify
from flask_cors import *
from sqlalchemy.exc import IntegrityError

from app.helpers.parse_order import parse_order
from app.solver.greedy_solver import GreedySolver
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


def get_and_check_order() -> Order:
    try:
        order = Order(**request.json)
    except TypeError:
        raise OrderValidException("invalidJson")
    return order


def order_exception_to_response(e: OrderValidException):
    return jsonify({"error": e.message_key, "variant": e.variant}), 400


@app.route("/order", methods=["POST"])
def add_order():
    try:
        order = get_and_check_order()
    except OrderValidException as e:
        return order_exception_to_response(e)
    order_dict = dict(order)
    del order_dict["id"]
    try:
        order.id = orders.insert(order_dict)
    except IntegrityError as e:
        return jsonify({"error": "userExists"}), 400
    return jsonify(order)


def check_order_edit_key(order_id: int, edit_key: str):
    """Returns a response if the order edit key is invalid, None otherwise"""
    order_from_db = orders.find_one(id=order_id)
    if order_from_db is None:
        return jsonify({"error": "orderNotFound"}), 404
    if order_from_db["edit_key"] != edit_key:
        return jsonify({"error": "wrongEditKey"}), 403
    return None


@app.route("/order", methods=["PUT"])
def update_order():
    try:
        order = get_and_check_order()
    except OrderValidException as e:
        return order_exception_to_response(e)
    response = check_order_edit_key(order.id, order.edit_key)
    if response is not None:
        return response
    orders.update(dict(order), ["id"])
    return jsonify(order)


@app.route("/order/<int:id>", methods=["DELETE"])
def delete_order(id: int):
    response = check_order_edit_key(id, request.json["edit_key"])
    if response is not None:
        return response
    orders.delete(id=id)
    return "", 204


def get_all_orders_without_edit_keys() -> List[Order]:
    """Returns all orders from the database, without edit keys"""
    result_orders = []
    for order in orders:
        result_orders.append(parse_order(order))
        result_orders[-1].edit_key = None
    return result_orders


@app.route("/order")
def get_orders():
    return jsonify(get_all_orders_without_edit_keys())


@app.route("/solved")
def solved():
    solver = GreedySolver()
    pizzas = solver.solve(get_all_orders_without_edit_keys())
    return jsonify([dict(pizza) for pizza in pizzas])


@app.route("/clear", methods=["POST"])
def clear_orders():
    if request.json["password"] == "JulianIstToll":
        orders.delete()
        return "", 204
    return jsonify({"error": "wrong password"}), 403


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
