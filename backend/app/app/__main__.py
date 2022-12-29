from flask import Flask, redirect
from flask_socketio import SocketIO
from flask_cors import *
import dataset

app = Flask(
    __name__,
    static_folder="../../../frontend/public",
    static_url_path="/static",
)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*") # , engineio_logger=True, logger=True)
db = dataset.connect(
    'sqlite:///db.sqlite', engine_kwargs={"connect_args": {'check_same_thread': False}})

@app.route("/")
def index():
    return "Hi"

if __name__ == "__main__":
    socketio.run(
        app, 
        host="0.0.0.0", 
        port=5113,
        debug=True, 
        use_reloader=True,
    )
