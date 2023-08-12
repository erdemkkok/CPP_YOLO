# CPP_YOLO

- Run yolo algorithms with .pt files

# USAGE
- you have to download yolov5 or another versions pt file.
- git clone https://github.com/ultralytics/yolov5  # clone
- cd yolov5
- sudo rm -rf export.py  && copy export.py from CPP_YOLO to yolov5 file
- python3 export.py torchcript yolov5.pt
- And path to exported file main.cpp
- Build that code with ROS-> colcon build or gcc
- And run it .
- İf you want you can use with crow server codes
