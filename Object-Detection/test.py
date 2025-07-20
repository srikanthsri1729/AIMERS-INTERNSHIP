from ultralytics import YOLO

# Load a model
model = YOLO("agriculture.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model(["kiwi.webp"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    print(result)
    result.save(filename="result.jpg")  # save to disk