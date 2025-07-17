from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def hello():
    return "Socket.IO server is running!"

@socketio.on('message')
def handle_message(data):
    print("Received message:", data)
    emit('response', {'status': 'received'})

# Add your own events here as needed, matching C++ client event names.

if __name__ == "__main__":
    # For HTTP:
    socketio.run(app, host="0.0.0.0", port=5000)
    # For HTTPS (uncomment below and provide cert files):
    # socketio.run(app, host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
