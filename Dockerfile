# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "dvc[gdrive]"

# initialise dvc
# RUN dvc init --no-scm
# configuring remote server in dvc
RUN dvc remote add -d storage gdrive://1svmfExACRXGTFXAplocJnDW-xUtC0C5c
RUN dvc remote modify storage gdrive_use_service_account true
RUN dvc remote modify storage gdrive_service_account_json_file_path creds.json

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# pulling the trained model
RUN dvc pull models/yolov8l-pose.pt.dvc

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
