detections = [
    {"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
    {"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
    {"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
    {"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
    {"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
]

def is_valid(item):
    return item["object"] == "human" and item["confidence"] > 85

humans = list(filter(is_valid, detections))

def get_distance(item):
    return item["distance"]

distances = list(map(get_distance, humans))

print("Human Detections:")
print(humans)

print("\nDistances:")
print(distances)

for d in distances:
    if d < 1:
        print("Alert: Human is very close")
    else:
        print("Human detected safely")