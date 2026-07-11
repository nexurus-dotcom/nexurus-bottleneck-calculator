import json

# Gaming CPU performance index
# Higher = better gaming performance

cpus = {

    # AMD Ryzen

    "AMD Ryzen 5 3600": 45,
    "AMD Ryzen 5 5600": 55,
    "AMD Ryzen 5 5600X": 57,
    "AMD Ryzen 5 7600": 65,
    "AMD Ryzen 5 7600X": 67.3,
    "AMD Ryzen 5 7600X3D": 80.6,
    "AMD Ryzen 5 9600X": 72.6,

    "AMD Ryzen 7 3700X": 50,
    "AMD Ryzen 7 5700X": 62,
    "AMD Ryzen 7 5800X": 70,
    "AMD Ryzen 7 5800X3D": 82,
    "AMD Ryzen 7 7700X": 70.6,
    "AMD Ryzen 7 7800X3D": 85.6,
    "AMD Ryzen 7 9800X3D": 97,
    "AMD Ryzen 7 9850X3D": 100,

    "AMD Ryzen 9 5900X": 68,
    "AMD Ryzen 9 5950X": 70,
    "AMD Ryzen 9 7900X": 69.2,
    "AMD Ryzen 9 7900X3D": 77.1,
    "AMD Ryzen 9 7950X": 71,
    "AMD Ryzen 9 7950X3D": 83.9,
    "AMD Ryzen 9 9900X": 73.9,
    "AMD Ryzen 9 9900X3D": 86.9,
    "AMD Ryzen 9 9950X": 76.9,
    "AMD Ryzen 9 9950X3D": 95.7,


    # Intel Core

    "Intel Core i5-10400": 45,
    "Intel Core i5-10600K": 52,
    "Intel Core i5-11400": 50,
    "Intel Core i5-11600K": 55,

    "Intel Core i5-12400": 58,
    "Intel Core i5-12600K": 60.8,
    "Intel Core i5-13400": 62,
    "Intel Core i5-13600K": 70.9,
    "Intel Core i5-14400": 58,
    "Intel Core i5-14600K": 72.8,

    "Intel Core i7-10700K": 55,
    "Intel Core i7-11700K": 60,
    "Intel Core i7-12700K": 65.8,
    "Intel Core i7-13700K": 75.8,
    "Intel Core i7-14700K": 76.4,

    "Intel Core i9-10900K": 62,
    "Intel Core i9-11900K": 63,
    "Intel Core i9-12900K": 70,
    "Intel Core i9-13900K": 76.8,
    "Intel Core i9-14900K": 78.2,

    # Intel Core Ultra

    "Intel Core Ultra 5 225": 62.5,
    "Intel Core Ultra 5 245K": 67.1,
    "Intel Core Ultra 5 250K Plus": 73.3,

    "Intel Core Ultra 7 265K": 70.3,
    "Intel Core Ultra 7 270K Plus": 77.5,

    "Intel Core Ultra 9 285K": 71.8
}

# Gaming GPU performance index

gpus = {

    "NVIDIA RTX 5090": 100,
    "NVIDIA RTX 4090": 90.1,
    "NVIDIA RTX 5080": 81.9,
    "AMD RX 7900 XTX": 79.3,
    "NVIDIA RTX 4080 Super": 78,
    "NVIDIA RTX 4080": 77.2,
    "NVIDIA RTX 5070 Ti": 76.2,
    "AMD RX 9070 XT": 76.9,
    "AMD RX 7900 XT": 71.3,
    "NVIDIA RTX 4070 Ti Super": 69.3,
    "AMD RX 9070": 69.1,
    "NVIDIA RTX 3090 Ti": 64.7,
    "NVIDIA RTX 4070 Ti": 66.3,
    "NVIDIA RTX 5070": 65.1,
    "NVIDIA RTX 3090": 60.3,
    "NVIDIA RTX 4070 Super": 62.2,
    "AMD RX 6950 XT": 60.5,
    "NVIDIA RTX 3080 Ti": 58.7,
    "AMD RX 9070 GRE": 59.2,
    "AMD RX 7800 XT": 58.1,
    "AMD RX 6900 XT": 57.4,
    "NVIDIA RTX 3080": 54.8,
    "AMD RX 6800 XT": 54.9,
    "NVIDIA RTX 4070": 54.7,
    "NVIDIA RTX 5060 Ti 16GB": 51.6,
    "AMD RX 7700 XT": 50.5,
    "AMD RX 9060 XT 16GB": 48.2,
    "NVIDIA RTX 5060 Ti 8GB": 49.3,
    "NVIDIA RTX 3070 Ti": 46.4,
    "AMD RX 9060 XT 8GB": 45.7,
    "NVIDIA RTX 4060 Ti 16GB": 43.8,
    "AMD RX 7600 XT": 50.1,
    "NVIDIA RTX 3070": 42.8,
    "NVIDIA RTX 4060 Ti 8GB": 43.2,
    "AMD RX 6750 XT": 40.8,
    "NVIDIA RTX 5060": 43.4,
    "AMD RX 6700 XT": 38.9,
    "Intel Arc B580": 35.1,
    "NVIDIA RTX 3060 Ti": 36.4,
    "NVIDIA RTX 4060": 35.1,
    "AMD RX 7600": 34.3,
    "NVIDIA RTX 5050": 34,
    "Intel Arc B570": 31.1,
    "NVIDIA RTX 3060 12GB": 30.2,
    "AMD RX 6650 XT": 31.5,
    "AMD RX 6600 XT": 30.8,
    "AMD RX 6600": 25.5,
    "NVIDIA RTX 3050": 21.9
}

with open("cpus.json", "w") as f:
    json.dump(cpus, f, indent=2)


with open("gpus.json", "w") as f:
    json.dump(gpus, f, indent=2)


print("✅ Gaming CPU and GPU databases created!")
print(f"CPUs: {len(cpus)}")
print(f"GPUs: {len(gpus)}")