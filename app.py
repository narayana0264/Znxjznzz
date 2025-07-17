from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route('/')
def hello():
    return "Hello, Socket.IO!"

@socketio.on("mobile_register")
def handle_register(data):
    print("Received:", data)
    socketio.emit("mobile_register_response", {"status": "ok"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
