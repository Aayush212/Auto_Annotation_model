from ultralytics import YOLO

# Load the trained model
model = YOLO(r'Path to best.pt')

# Perform inference
results = model.predict(
    source=r'Path to test images folder',
    save=True,
    imgsz=640
)

# Display results
for result in results:
    print(result.boxes)
