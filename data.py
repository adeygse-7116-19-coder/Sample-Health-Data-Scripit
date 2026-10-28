
# Sample Health Data
# Educational example using fictional patient records.

patients = [
    {
        "patient_id": "P001",
        "age": 25,
        "temperature_c": 36.8,
        "heart_rate_bpm": 72
    },
    {
        "patient_id": "P002",
        "age": 40,
        "temperature_c": 37.1,
        "heart_rate_bpm": 80
    },
    {
        "patient_id": "P003",
        "age": 32,
        "temperature_c": 36.6,
        "heart_rate_bpm": 68
    }
]

print("SAMPLE HEALTH DATA")
print("------------------")

for patient in patients:
    print("Patient ID:", patient["patient_id"])
    print("Age:", patient["age"])
    print("Temperature:", patient["temperature_c"], "C")
    print("Heart rate:", patient["heart_rate_bpm"], "bpm")
    print()
