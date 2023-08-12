from ultralytics import YOLO

# Load a model
model = YOLO('/home/erdem/cpp_yolo_Conf/yolov8n.pt')  # load an official model
#model = YOLO('path/to/best.pt')  # load a custom trained

# Export the model
model.export(format='torchscript')