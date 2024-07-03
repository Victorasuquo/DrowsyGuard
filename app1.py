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
cap = cv2.VideoCapture("test.mp4")  # Replace 0 with the path to your video file if you want to process a video file

# while True:
#     # Read the frame from the video capture
#     ret, frame = cap.read()

#     # Perform object detection on the frame
#     results = model(frame)

#     # Visualize the detections on the frame
#     output_frame = results.render()

#     # Display the frame with the detections
#     cv2.imshow('Object Detection', output_frame)

#     # Check for the 'q' key to exit the loop
#     if cv2.waitKey(1) == ord('q'):
#         break
# while True:
#     ret, frame = cap.read()
#     results = model(frame, agnostic_nms=True)[0]

#     if not results or len(results) == 0:
#         continue

#     for result in results:

#         detection_count = result.boxes.shape[0]

#         for i in range(detection_count):
#             cls = int(result.boxes.cls[i].item())
#             name = result.names[cls]
#             confidence = float(result.boxes.conf[i].item())
#             bounding_box = result.boxes.xyxy[i].cpu().numpy()

#             x = int(bounding_box[0])
#             y = int(bounding_box[1])
#             width = int(bounding_box[2] - x)
#             height = int(bounding_box[3] - y)

#     # check for the 'q' key to exit the loop
#     if cv2.waitKey(1) == ord('q'):
#         break
# # Release the video capture and close the OpenCV windows
# cap.release()
# # cv2.destroyAllWindows()
# import cv2
# from ultralytics import YOLO

# # Load the YOLO model
# model = YOLO('best.pt')

# # Open the video capture
# cap = cv2.VideoCapture("test.mp4")  # Replace with your video file path

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Perform object detection on the frame
#     results = model(frame, agnostic_nms=True)[0]

# #     if results.pred[0] is not None:
#         for item in results.pred[0]:
#             # Extract information from the detection result
#             class_id = int(item[5])
#             class_name = model.names[class_id]
#             confidence = float(item[4])
#             bbox = item[:4]

#             # Draw bounding box and label on the frame
#             x1, y1, x2, y2 = map(int, bbox)
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             cv2.putText(frame, f'{class_name} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#     # Display the frame with detections
#     cv2.imshow('Object Detection', frame)

#     # Check for the 'q' key to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Open the video capture
cap = cv2.VideoCapture(0)  # Replace with your video file path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform object detection on the frame
    results = model(frame, agnostic_nms=True)
    
    # Iterate through the results
    for result in results:
        boxes = result.boxes
        names = result.names

        for box in boxes:
            # Extract bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Get the class id and confidence score
            class_id = int(box.cls)
            confidence = float(box.conf)
            class_name = names[class_id]

            # Draw bounding box and label on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'{class_name} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame with detections
    cv2.imshow('Object Detection', frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

