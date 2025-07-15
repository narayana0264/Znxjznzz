from flask import Flask, request
from flask_socketio import SocketIO
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

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

if __name__ == "__main__":
    logger.info("Starting Flask-SocketIO server on http://0.0.0.0:8000")
    socketio.run(app, host='0.0.0.0', port=port)
