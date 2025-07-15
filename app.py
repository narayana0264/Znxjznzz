<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Flask-SocketIO Test</title>
  <script src="https://cdn.socket.io/4.6.1/socket.io.min.js"></script>
</head>
<body>
  <h2>Flask-SocketIO Client Test</h2>
  <button onclick="sendRegisterValid()">Send Valid Register</button>
  <button onclick="sendRegisterInvalid()">Send Invalid Register</button>
  <pre id="output"></pre>

  <script>
    const output = document.getElementById("output");

    const socket = io("https://socketio-m94h.onrender.com", {
      transports: ["websocket"]
    });

    socket.on("connect", () => {
      log("✅ Connected to server");
    });

    socket.on("disconnect", () => {
      log("❌ Disconnected from server");
    });

    socket.on("mobile_register_response", (data) => {
      log("📨 Response: " + JSON.stringify(data));
    });

    function sendRegisterValid() {
      const payload = {
        organisation_id: "xyz",     // triggers "FINE"
        username: "myuser@example.com"
      };
      socket.emit("mobile_register", payload);
      log("📤 Sent valid registration: " + JSON.stringify(payload));
    }

    function sendRegisterInvalid() {
      const payload = {
        organisation_id: "abc",     // triggers "BE CAREFULL"
        username: "test@example.com"
      };
      socket.emit("mobile_register", payload);
      log("📤 Sent invalid registration: " + JSON.stringify(payload));
    }

    function log(msg) {
      output.textContent += msg + "\n";
      console.log(msg);
    }
  </script>
</body>
</html>
