import cv2
import numpy as np
import os

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the webcam feed
cap = cv2.VideoCapture(0)  # 0 for the default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit the application")

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Get the face region of interest (ROI)
        face_roi = frame[y:y + h, x:x + w]

        # Skip small faces
        if face_roi.shape[0] < 50 or face_roi.shape[1] < 50:
            continue

        # Simple age estimation based on face size
        face_size = w * h
        if face_size > 100000:  # Large face
            age = "Adult"
        else:
            age = "Young"

        # Simple gender estimation (this is just a placeholder)
        gender = "Person"

        # Display age and gender on the frame
        label = f'{gender}, {age}'
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Show the frame with detections
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
