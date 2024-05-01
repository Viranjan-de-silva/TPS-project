import cv2
import constants as c

mouseX, mouseY = 0, 0
pause = False

def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_MOUSEMOVE:
        mouseX, mouseY = x, y


video_path = 'sample_clips/new3.mp4'  # video width = 2560, height = 1440
cap = cv2.VideoCapture(video_path)



cv2.namedWindow('full frame', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('full frame', draw_circle)

while cap.isOpened():
    if not pause:
        ret, frame = cap.read()
    if not ret:
        break  # End of video

    #showing pixel coordinate
    cv2.putText(frame, "Coordinates: x={} y={}".format(mouseX, mouseY), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255), 2)

    #----------------------Truck lane lines---------------------------------------
    cv2.line(frame, c.HLstart_point, c.HLend_point, c.line_color, c.thickness)
    cv2.line(frame, c.L1start, c.L1end, c.line_color, c.thickness)
    cv2.line(frame, c.L2start, c.L2end, c.line_color, c.thickness)
    cv2.line(frame, c.L3start, c.L3end, c.line_color, c.thickness)
    cv2.line(frame, c.L4start, c.L4end, c.line_color, c.thickness)
    cv2.line(frame, c.L5start, c.L5end, c.line_color, c.thickness)

    #--------------------Alignment lines----------------------------
    cv2.line(frame, c.lane5_start, c.lane5_end, c.alignment_line_color, c.thickness)
    cv2.line(frame, c.lane4_start, c.lane4_end, c.alignment_line_color, c.thickness)
    cv2.line(frame, c.lane2_start, c.lane2_end, c.alignment_line_color, c.thickness)
    cv2.line(frame, c.lane3_start, c.lane3_end, c.alignment_line_color, c.thickness)

    cv2.imshow('full frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(' '):
        pause = not pause

cap.release()
cv2.destroyAllWindows()
