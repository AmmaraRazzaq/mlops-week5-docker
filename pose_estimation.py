from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("yolov8l-pose.pt")  # load an official model

image_path = "selected_frames/User_Submission_43_Lorenzo.png"
image = cv2.imread(image_path)

# Predict with the model
pose_results = model(image)[0]  # predict on an image
keypoints = pose_results.keypoints.xy.cpu().numpy().astype('int')[0]

# annotated_frame = pose_results.plot()
# cv2.imwrite("pose_inference/pose_estimation.png", annotated_frame)

if len(keypoints) > 0:
    print("person found")
else:
    print("no person found")
    