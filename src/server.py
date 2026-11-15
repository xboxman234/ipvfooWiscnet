from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/lookup", methods=["POST"])
def lookup_ips():
    data = request.get_json()          # Reads the JSON sent by your extension
    data=data.get("ips", [])
    testList = ["192.178.214.95"]
    # Process the IPs here
    results = [ip in testList  for ip in data]

    return jsonify({"results": results})

if __name__ == "__main__":
    # Runs locally at http://127.0.0.1:5000
    app.run(port=5000, debug=True)