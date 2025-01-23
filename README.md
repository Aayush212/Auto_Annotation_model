YOLOv8 Custom Object Detection Project

This repository contains the code and configurations for training, validating, and performing inference using a custom-trained YOLOv8 model for binary classification (ok and notok).

Project Overview

Model: YOLOv8n (custom-trained).

Dataset: Contains images for training, validation, and testing, organized into separate folders.

Classes:
    
     ok
     notok

Repository Structure

model.py:   Script for training the YOLOv8 model on the custom dataset.

infer.py:   Script for running inference on test images using the trained model.

data.yaml:  Configuration file specifying dataset paths and class names.

Setup Instructions

1. Install Dependencies

Ensure you have Python installed. Install the required libraries using:

    bash

    pip install ultralytics

2. Dataset Structure

Organize your dataset as specified in data.yaml:

    bash

    Dataset/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    └── test/
    ├── images/
    └── labels/

3. Training the Model

Run model.py to train the YOLOv8 model:

    bash

    python model.py

Key Parameters:

data:     Path to data.yaml.

epochs:     Number of training epochs (default: 50).

imgsz:      Image size for training (default: 640x640).

batch:      Batch size (default: 16).

4. Inference

Run infer.py to perform inference on test images:

    bash

    python infer.py

Key Parameters:

source: Path to the folder containing test images.

save: Save results (set to True).

imgsz: Image size for inference (default: 640x640).

5. Model Export

The trained model can be exported to the ONNX format for deployment:

    bash

    model.export(format='onnx')

Configuration Files

data.yaml

Specifies dataset paths and class names:

    yaml

    train: C:/path/to/train/images
    val: C:/path/to/valid/images
    test: C:/path/to/test/images

    nc: 2
    names: ['ok', 'notok']

Results

Training Metrics: Training accuracy, loss, and other metrics are logged in the runs/train directory.

Inference Results: Saved in the specified directory with bounding boxes and class predictions.
