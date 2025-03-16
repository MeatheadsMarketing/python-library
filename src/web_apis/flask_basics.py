from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """Example API endpoint for AI predictions"""
    data = request.get_json()
    result = np.array(data["input"]) * 2  # Example transformation
    return jsonify({"prediction": result.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
