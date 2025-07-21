from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Stored sentence
SENTENCE = "if"

@app.route('/sentence', methods=['GET'])
def get_sentence():
    return jsonify({"sentence": SENTENCE})

@app.route('/keystrokes', methods=['POST'])
def save_keystrokes():
    data = request.get_json()  # Expect list of dicts
    if not data:
        return jsonify({"error": "No data provided"}), 400

    output_file = 'keystrokes.csv'

    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Key', 'DownTime_ms', 'UpTime_ms'])  # Header
            for item in data:
                writer.writerow([
                    item.get('key', ''),
                    item.get('down_time_ms', ''),
                    item.get('up_time_ms', '')
                ])
    except Exception as e:
        return jsonify({"error": f"Failed to write file: {str(e)}"}), 500

    return jsonify({"message": "Data saved to CSV"}), 200

if __name__ == '__main__':
    # Listen on all network interfaces (Wi-Fi, LAN, etc.)
    app.run(host='0.0.0.0', port=5000, debug=True)
