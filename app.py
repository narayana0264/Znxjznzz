from flask import Flask, request
from flask_socketio import SocketIO
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Enable debug logging for socketio and engineio
logging.getLogger("socketio").setLevel(logging.DEBUG)
logging.getLogger("engineio").setLevel(logging.DEBUG)

# Create Flask app
app = Flask(__name__)

# Initialize SocketIO with eventlet and Engine.IO v3 for C++ compatibility
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="eventlet",
    engineio_protocol=3  # REQUIRED for C++ client compatibility
)

# Event handler for mobile_register
@socketio.on("mobile_register")
def handle_mobile_register(data):
    logger.info("Received mobile_register event: %s", data)
    
    organisation_id = data.get("organisation_id")
    username = data.get("username")

    if not organisation_id or not username:
        logger.warning("Missing required fields: organisation_id=%s, username=%s", organisation_id, username)
        socketio.emit("mobile_register_response", {
            "error": "Please provide required fields"
        }, room=request.sid)
        return

    if organisation_id == "xyz":
        logger.info("Valid organisation_id: %s, sending response: FINE", organisation_id)
        socketio.emit("mobile_register_response", {
            "message": "FINE"
        }, room=request.sid)
    else:
        logger.info("Invalid organisation_id: %s, sending response: BE CAREFULL", organisation_id)
        socketio.emit("mobile_register_response", {
            "message": "BE CAREFULL"
        }, room=request.sid)

# Start the server
if __name__ == "__main__":
    logger.info("Starting Flask-SocketIO server...")
    port = int(os.environ.get("PORT", 10000))  # Use Render's PORT or default to 10000
    socketio.run(app, host="0.0.0.0", port=port)
