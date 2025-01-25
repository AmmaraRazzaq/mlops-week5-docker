from fastapi import FastAPI
app = FastAPI(title="Pose Estimation App")

from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("yolov8l-pose.pt")  # load an official model

@app.get("/")
async def home():
    return "<h2>This is a pose estimation app for Golfers</h2>"


@app.get("/predict")
async def get_prediction(image_path):
    image = cv2.imread(str(image_path))

    # Predict with the model
    pose_results = model(image)[0]  # predict on an image
    keypoints = pose_results.keypoints.xy.cpu().numpy().astype('int')[0]

    # annotated_frame = pose_results.plot()
    # cv2.imwrite("pose_inference/pose_estimation.png", annotated_frame)

    if len(keypoints) > 0:
        return "person found"
    else:
        return "no person found"

