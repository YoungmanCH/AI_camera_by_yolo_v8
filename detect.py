from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

    # Process the frame with YOLO model
predict_result = model.predict(0, save=True, show=True, task='segment')


