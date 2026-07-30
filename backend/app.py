import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api")
def api():
    return jsonify({
        "message": "hello from my backend",
        "app_name": os.getenv("APP_NAME", "unknown"),
        "environment": os.getenv("ENVIRONMENT", "unknown")
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
