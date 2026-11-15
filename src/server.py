from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/lookup", methods=["POST"])
def lookup_ips():
    data = request.get_json()          # Reads the JSON sent by your extension
    ip_list = data.get("ips", [])      # Extracts ["1.1.1.1", "8.8.8.8"]

    # Process the IPs here
    results = [{"ip": ip, "status": "checked"} for ip in ip_list]

    return jsonify({"results": results})

if __name__ == "__main__":
    # Runs locally at http://127.0.0.1:5000
    app.run(port=5000, debug=True)