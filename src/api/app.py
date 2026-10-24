from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")
model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    else:
        print(f"WARNING: no model at {MODEL_PATH}")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "model not loaded"}), 503
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "missing 'text' field"}), 400
    proba = model.predict_proba([text])[0]
    label = "positive" if proba[1] >= 0.5 else "negative"
    return jsonify({"text": text, "label": label, "score": float(proba[1])})

if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
