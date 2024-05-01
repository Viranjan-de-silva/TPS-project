import cv2

# Callback Function for Mouse, Circle
def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_MOUSEMOVE:
        mouseX, mouseY = x, y

# Load the video
cap = cv2.VideoCapture('sample_clips/lane4.mp4')

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('frame', draw_circle)

mouseX, mouseY = 0, 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.putText(frame, "Coordinates: x={} y={}".format(mouseX, mouseY), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key == ord(' '):
            cv2.waitKey(-1)

        if key == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
