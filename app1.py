# from ultralytics import YOLO
#
# model = YOLO('best.pt')
# output = model.predict(source='up.jpg', show=True, conf=0.2)
# output.save()

import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Open the video capture
cap = cv2.VideoCapture('up.jpg')  # Replace 0 with the path to your video file if you want to process a video file

while True:
    # Read the frame from the video capture
    ret, frame = cap.read()

    # Perform object detection on the frame
    results = model(frame)

    # Visualize the detections on the frame
    output_frame = results.render()

    # Display the frame with the detections
    cv2.imshow('Object Detection', output_frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
