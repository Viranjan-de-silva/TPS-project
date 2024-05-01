import cvzone
import cv2

def IdentifyLane(points, frame, laneNo):
    lane = '0'

    maxx = 0
    minx = 3000

    maxy = 0
    miny = 3000

    for i in range (len(points)):
        if maxx < points[i][0][0]:   # finding maximum x coordinate
            maxx = points[i][0][0]
            maxx_y = points[i][0][1]

        if points[i][0][0] < minx:  # finding minimum x coordinate
            minx = points[i][0][0]
            minx_y = points[i][0][1]

        if maxy < points[i][0][1]:  # finding maximum y coordinate
            maxy = points[i][0][1]
            maxy_x = points[i][0][0]

        if points[i][0][1] < miny:  # finding minimum y coordinate
            miny = points[i][0][1]
            miny_x = points[i][0][0]

    mid_coordinate = ((minx+maxx)/2,((minx_y+maxx_y)/2)*-1)
    # cv2.line(frame, (maxx, maxx_y), (minx, minx_y), (255, 255, 0), 6)
    # print(mid_coordinate[0])

    if mid_coordinate[0] < 1265 :
        # lane = '2' #or 5
        comparison_val = 193*mid_coordinate[1]-910*mid_coordinate[0]+1103290 #line2
        if comparison_val > 0:
            # lane = '2'
            comparison_val = 75*mid_coordinate[1]-182*mid_coordinate[0]+201730 #line1
            if comparison_val < 0:
                lane = '2'
            else:
                lane = 'undefined'
        elif comparison_val < 0:
            lane = '3'
        else:
            lane = 'undefined'


    elif mid_coordinate[0] > 1265 :
        # lane = '4' #or 5
        comparison_val = 310 * mid_coordinate[1] + 910 * mid_coordinate[0] - 1168850  # line4
        if comparison_val > 0:
            # lane = '5'
            comparison_val = 475 * mid_coordinate[1] + 910 * mid_coordinate[0] - 1281600 # line5
            if comparison_val < 0:
                lane = '5'
            else:
                lane = 'undefined'
        elif comparison_val < 0:
            lane = '4'
        else:
            lane = 'undefined'
    else:
        lane = 'undefined'

    if laneNo == lane:
        cvzone.putTextRect(frame, f'{lane}',
                       (max(0, maxx), max(35, maxx_y)), scale=4, thickness=3, colorB=(0,0,255),
                       colorT=(255, 255, 255), colorR=(0,255,0), offset=5)
    else:
        cvzone.putTextRect(frame, f'{lane}',
                           (max(0, maxx), max(35, maxx_y)), scale=4, thickness=3, colorB=(0, 0, 255),
                           colorT=(255, 255, 255), colorR=(0, 0, 255), offset=5)
    return lane
