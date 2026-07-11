from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("cpus.json") as f:
    cpus = json.load(f)

with open("gpus.json") as f:
    gpus = json.load(f)

def find_score(name, data):
    for item_name, score in data.items():
        if name.lower() in item_name.lower():
            return score
    return None

@app.route('/')
def home():
    return "Nexurus Bottleneck Calculator API is running!"

@app.route("/cpus")
def get_cpus():
    return jsonify(list(cpus.keys()))


@app.route("/gpus")
def get_gpus():
    return jsonify(list(gpus.keys()))

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    cpu_name = data.get("cpu")
    gpu_name = data.get("gpu")

    cpu_score = find_score(cpu_name, cpus)
    gpu_score = find_score(gpu_name, gpus)

    if not cpu_score or not gpu_score:
        return jsonify({"error": "Part not found"}), 400

    ratio = cpu_score / gpu_score

    if ratio < 0.8:
        result = "CPU bottleneck"
    elif ratio > 1.2:
        result = "GPU bottleneck"
    else:
        result = "Balanced"

    return jsonify({
        "cpu_score": cpu_score,
        "gpu_score": gpu_score,
        "ratio": round(ratio, 2),
        "result": result
    })

if __name__ == "__main__":
    app.run()