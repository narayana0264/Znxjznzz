from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def hello():
    return "Socket.IO server is running!"

@socketio.on("message")
def handle_message(data):
    print("Received message:", data)
    emit("response", {"status": "received"})

# Add any other events your C++ client expects here.

if __name__ == "__main__":
    # For local dev only. For Render/Railway use gunicorn as below.
    socketio.run(app, host="0.0.0.0", port=5000)
