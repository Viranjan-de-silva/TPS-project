import cv2
import numpy as np
from ultralytics import YOLO
import math
import cvzone
import constants as c
import laneFunction as lf
import Alignment as al

# Load your custom YOLOv8l-seg model
model = YOLO('best.pt')

# Read the video clip (replace 'your_video.mp4' with your actual video file)
video_path = 'sample_clips/new4.mp4'
cap = cv2.VideoCapture(video_path)

# Define colors for each class
colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0), (0, 255, 255)]  # Green, Red, Blue, Yellow
classNames = ["40ft", "20ft", "d20ft", "trailer"]
myColor = (0, 0, 255)

while True:
    laneNo = str(input("Enter lane No : "))
    if laneNo == 'q':
        break
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        c.drawTruckLanes(frame)

        # Predict segmentations
        results = model.track(source=frame.copy(), save=False, save_txt=False, imgsz=640)

        #==================================================================================================================
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box===================================================================================
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                w, h = x2 - x1, y2 - y1
                # cvzone.cornerRect(img, (x1, y1, w, h))

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Class Name
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                # print(currentClass)

                cvzone.putTextRect(frame, f'{classNames[cls]} {conf}',
                                   (max(0, x1), max(35, y1)), scale=3, thickness=2, colorB=myColor,
                                   colorT=(255, 255, 255), colorR=myColor, offset=5)
                cv2.rectangle(frame, (x1, y1), (x2, y2), myColor, 3)
        #============================================================================================================

        # Extract masks for each object
        class_ids = np.array(results[0].boxes.cls.cpu(), dtype=int)

        # Draw contours on the frame
        contour_frame = frame.copy()
        for i in range(len(class_ids)):
            empty_image = np.zeros(frame.shape[:3], dtype=np.uint8)
            res_plotted = results[0][i].plot(boxes=0, img=empty_image)
            # Convert the mask to binary format
            _, binary_mask = cv2.threshold(res_plotted[:, :, 0], 1, 255, cv2.THRESH_BINARY)

            # Find contours
            contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                # Approximate contour to polygon
                epsilon = 0.012* cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)

                # Draw contours with color corresponding to the class
                cv2.drawContours(contour_frame, [approx], -1, colors[class_ids[i] % len(colors)], 2)
                # print("Vertices:", approx)
                if len(approx) > 0:
                    # print(len(approx))
                    lane = lf.IdentifyLane(approx, contour_frame, laneNo)
                    # print("The lane is ", lane)
                    midpoint = al.getMidPoint(approx)
                    print(midpoint)
                    cv2.circle(contour_frame, midpoint, 10, (0,0,255), -1)
                    if lane == laneNo:
                        print("The lane is ", lane)
                        print("Vertices:", approx)
                        print(al.getDistance(midpoint, laneNo))

            # Draw contours with color corresponding to the class
            # cv2.drawContours(contour_frame, contours, -1, colors[class_ids[i] % len(colors)], 2)

        # Display the result
        cv2.namedWindow('full_frame', cv2.WINDOW_NORMAL)
        cv2.imshow('full_frame', contour_frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    cv2.destroyAllWindows()
# Release video capture
cap.release()