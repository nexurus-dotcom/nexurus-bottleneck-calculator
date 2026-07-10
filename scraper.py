import json

# TEMPORARY manual data (so we know it works)
cpus = {
    "Intel Core i5-10400": 12500,
    "Intel Core i7-10700K": 17000,
    "AMD Ryzen 5 5600X": 16000
}

gpus = {
    "NVIDIA GTX 1660": 10000,
    "NVIDIA RTX 3060": 17000,
    "AMD RX 6600": 15000
}

# Save to files
with open("cpus.json", "w") as f:
    json.dump(cpus, f, indent=2)

with open("gpus.json", "w") as f:
    json.dump(gpus, f, indent=2)

print("✅ Data saved successfully!")