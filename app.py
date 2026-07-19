from flask import Flask, request, jsonify
from upgrade_database import gpu_upgrades, cpu_upgrades
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


    difference = cpu_score - gpu_score

    percent_diff = abs(difference) / max(cpu_score, gpu_score)


    if percent_diff < 0.15:
        result = "Balanced"

    elif difference > 0:
        result = "GPU bottleneck"

    else:
        result = "CPU bottleneck"


    match = max(0, 100 - (percent_diff * 100))

    ratio = round(match / 100, 2)


    return jsonify({
        "cpu_score": cpu_score,
        "gpu_score": gpu_score,
        "ratio": ratio,
        "result": result
    })


def clean_gpu_name(text):
    return (
        text.lower()
        .replace("nvidia", "")
        .replace("amd", "")
        .replace("geforce", "")
        .replace("radeon", "")
        .replace("graphics card", "")
        .strip()
    )


def clean_cpu_name(text):

    text = text.lower()

    replacements = [
        "amd",
        "intel",
        "processor",
        "cpu",
        "core",
        "ryzen",
        "™",
        "®"
    ]

    for item in replacements:
        text = text.replace(item, "")

    return (
        text
        .replace(" ", "")
        .replace("-", "")
        .strip()
    )


@app.route("/upgrades", methods=["POST"])
def get_upgrades():

    data = request.json
    gpu_input = data.get("gpu", "")

    upgrades = []

    cleaned_input = clean_gpu_name(gpu_input)

    for gpu_name in gpu_upgrades:

        if (
            clean_gpu_name(gpu_name) in cleaned_input
            or cleaned_input in clean_gpu_name(gpu_name)
        ):
            upgrades = gpu_upgrades[gpu_name]
            break

    return jsonify({
        "upgrades": upgrades
    })


@app.route("/cpu-upgrades", methods=["POST"])
def get_cpu_upgrades():

    data = request.json
    cpu_input = data.get("cpu", "")

    upgrades = []

    cleaned_input = clean_cpu_name(cpu_input)

    for cpu_name in cpu_upgrades:

        if (
            clean_cpu_name(cpu_name) in cleaned_input
            or cleaned_input in clean_cpu_name(cpu_name)
        ):
            upgrades = cpu_upgrades[cpu_name]
            break

    return jsonify({
        "upgrades": upgrades
    })


@app.route("/recommendations", methods=["POST"])
def recommendations():

    data = request.json

    cpu_name = data.get("cpu", "")
    gpu_name = data.get("gpu", "")


    cpu_score = find_score(cpu_name, cpus)
    gpu_score = find_score(gpu_name, gpus)


    if not cpu_score or not gpu_score:
        return jsonify({
            "error": "Part not found"
        }), 400


    difference = cpu_score - gpu_score

    upgrades = []


    percent_diff = abs(difference) / max(cpu_score, gpu_score)


    # Balanced
    if percent_diff < 0.15:

        result = "Balanced"
        recommendation_type = "None"


    # CPU is weaker = CPU bottleneck
    elif difference < 0:

        result = "CPU bottleneck"
        recommendation_type = "CPU"


        cleaned_input = clean_cpu_name(cpu_name)


        for cpu in cpu_upgrades:

            database_cpu = clean_cpu_name(cpu)

            if (
                database_cpu in cleaned_input
                or cleaned_input in database_cpu
            ):

                upgrades = cpu_upgrades[cpu]
                break


        if not upgrades:

            closest_cpu = None
            closest_difference = 999999


            for cpu in cpus:

                upgrade_difference = cpus[cpu] - cpu_score


                if (
                    upgrade_difference > 0
                    and upgrade_difference < closest_difference
                ):

                    closest_difference = upgrade_difference
                    closest_cpu = cpu


            if closest_cpu:
                upgrades = [closest_cpu]


    # GPU is weaker = GPU bottleneck
    else:

        result = "GPU bottleneck"
        recommendation_type = "GPU"


        cleaned_input = clean_gpu_name(gpu_name)


        for gpu in gpu_upgrades:

            database_gpu = clean_gpu_name(gpu)


            if (
                database_gpu in cleaned_input
                or cleaned_input in database_gpu
            ):

                upgrades = gpu_upgrades[gpu]
                break


        if not upgrades:

            closest_gpu = None
            closest_difference = 999999


            for gpu in gpus:

                upgrade_difference = gpus[gpu] - gpu_score


                if (
                    upgrade_difference > 0
                    and upgrade_difference < closest_difference
                ):

                    closest_difference = upgrade_difference
                    closest_gpu = gpu


            if closest_gpu:
                upgrades = [closest_gpu]


    return jsonify({

        "result": result,

        "recommendation_type": recommendation_type,

        "upgrades": upgrades

    })


if __name__ == "__main__":
    app.run()