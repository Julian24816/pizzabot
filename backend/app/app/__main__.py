from flask import Flask, request, jsonify
from flask_cors import *
import dataset

from .order import Order

app = Flask(
    __name__,
    static_folder="../../../frontend/public",
    static_url_path="/static",
)
CORS(app)
db = dataset.connect(
    'sqlite:///db.sqlite', engine_kwargs={"connect_args": {'check_same_thread': False}})
orders = db["orders"]


@app.route("/order", methods=["PUT"])
def add_order():
    try:
        order = Order(**request.json)
    except TypeError:
        return jsonify({"error": "Invalid order"}), 400
    order_dict = dict(order)
    del order_dict["id"]
    order.id = orders.insert(order_dict)
    return jsonify(order)


@app.route("/order", methods=["DELETE"])
def delete_order():
    order_id = request.json["id"]
    orders.delete(id=order_id)
    return "", 204


@app.route("/order")
def get_orders():
    return jsonify([Order(**order) for order in orders])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5113,
        debug=True,
        use_reloader=True,
    )
