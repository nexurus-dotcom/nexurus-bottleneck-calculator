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

    # NVIDIA RTX 50 Series

    "NVIDIA RTX 5090": 100,
    "NVIDIA RTX 5080": 81.9,
    "NVIDIA RTX 5070 Ti": 76.2,
    "NVIDIA RTX 5070": 65.1,
    "NVIDIA RTX 5060 Ti 16GB": 51.6,
    "NVIDIA RTX 5060 Ti 8GB": 49.3,
    "NVIDIA RTX 5060": 43.4,
    "NVIDIA RTX 5050": 34,


    # NVIDIA RTX 40 Series

    "NVIDIA RTX 4090": 90.1,
    "NVIDIA RTX 4080 Super": 78,
    "NVIDIA RTX 4080": 77.2,
    "NVIDIA RTX 4070 Ti Super": 69.3,
    "NVIDIA RTX 4070 Ti": 66.3,
    "NVIDIA RTX 4070 Super": 62.2,
    "NVIDIA RTX 4070": 54.7,
    "NVIDIA RTX 4060 Ti 16GB": 43.8,
    "NVIDIA RTX 4060 Ti 8GB": 43.2,
    "NVIDIA RTX 4060": 35.1,


    # NVIDIA RTX 30 Series

    "NVIDIA RTX 3090 Ti": 64.7,
    "NVIDIA RTX 3090": 60.3,
    "NVIDIA RTX 3080 Ti": 58.7,
    "NVIDIA RTX 3080": 54.8,
    "NVIDIA RTX 3070 Ti": 46.4,
    "NVIDIA RTX 3070": 42.8,
    "NVIDIA RTX 3060 Ti": 36.4,
    "NVIDIA RTX 3060 12GB": 30.2,
    "NVIDIA RTX 3060 8GB": 28,


    # NVIDIA RTX 20 Series

    "NVIDIA RTX 2080 Ti": 45,
    "NVIDIA RTX 2080 Super": 40,
    "NVIDIA RTX 2080": 38,
    "NVIDIA RTX 2070 Super": 34,
    "NVIDIA RTX 2070": 30,
    "NVIDIA RTX 2060 Super": 28,
    "NVIDIA RTX 2060": 25,


    # NVIDIA GTX 10 Series

    "NVIDIA GTX 1080 Ti": 35,
    "NVIDIA GTX 1080": 30,
    "NVIDIA GTX 1070 Ti": 25,
    "NVIDIA GTX 1070": 22,
    "NVIDIA GTX 1060 6GB": 18,
    "NVIDIA GTX 1060 3GB": 15,


    # NVIDIA GTX 16 Series

    "NVIDIA GTX 1660 Ti": 22,
    "NVIDIA GTX 1660 Super": 21,
    "NVIDIA GTX 1660": 20,


    # NVIDIA GTX 900 Series

    "NVIDIA GTX 980 Ti": 22,
    "NVIDIA GTX 980": 18,
    "NVIDIA GTX 970": 16,


    # NVIDIA RTX 30 Entry

    "NVIDIA RTX 3050 8GB": 21.9,


    # AMD RX 9000 Series

    "AMD RX 9070 XT": 76.9,
    "AMD RX 9070": 69.1,
    "AMD RX 9060 XT 16GB": 48.2,
    "AMD RX 9060 XT 8GB": 45.7,


    # AMD RX 7000 Series

    "AMD RX 7900 XTX": 79.3,
    "AMD RX 7900 XT": 71.3,
    "AMD RX 7800 XT": 58.1,
    "AMD RX 7700 XT": 50.5,
    "AMD RX 7600 XT": 50.1,
    "AMD RX 7600": 34.3,


    # AMD RX 6000 Series

    "AMD RX 6950 XT": 60.5,
    "AMD RX 6900 XT": 57.4,
    "AMD RX 6800 XT": 54.9,
    "AMD RX 6800": 50,
    "AMD RX 6750 XT": 40.8,
    "AMD RX 6700 XT": 38.9,
    "AMD RX 6650 XT": 31.5,
    "AMD RX 6600 XT": 30.8,
    "AMD RX 6600": 25.5,


    # Older AMD RX

    "AMD RX 5700 XT": 35,
    "AMD RX 5700": 30,
    "AMD RX 5600 XT": 25,
    "AMD RX 5500 XT": 20,
    "AMD RX 590": 18,
    "AMD RX 580": 15,


    # Intel Arc

    "Intel Arc B580": 35.1,
    "Intel Arc B570": 31.1
}

with open("cpus.json", "w") as f:
    json.dump(cpus, f, indent=2)


with open("gpus.json", "w") as f:
    json.dump(gpus, f, indent=2)


print("✅ Gaming CPU and GPU databases created!")
print(f"CPUs: {len(cpus)}")
print(f"GPUs: {len(gpus)}")