from ultralytics import YOLO

# Load YOLOv8n model 
model = YOLO(r'C:\Users\Amazin\ultralytics\yoloenv\runs\train\custom_yolov8n5\weights\best.pt')

# Train the model
model.train(
    data=r'C:\Users\Amazin\ultralytics\yoloenv\data.yaml', 
    epochs=50,                   
    imgsz=640,                   
    batch=16,                    # Batch size
    project='runs/train',        # Save results to runs/train
    name='custom_yolov8n',       # Model name
    pretrained=True,
    save_period = 1,
    resume = True
)

# Validate the model on the validation set
metrics = model.val(data='data.yaml')
print(metrics)

#exporting the model
model.export(format='onnx') 
#C:\Users\Amazin\ultralytics\yoloenv\runs\train\custom_yolov8n3\weights\best.pt

