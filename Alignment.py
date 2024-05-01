import math

def getMidPoint(points):

    maxx = 0
    maxx_y = 0
    minx = 3000
    minx_y = 0

    lower_points = []
    for i in range(len(points)):
        if points[i][0][1] > 1080:
            lower_points.append(points[i][0])


    if (len(lower_points) == len(points)) or (len(lower_points) == 0): # container is not yet came to alignment position
        return None
    else:
        extracted_points = [point.tolist() for point in lower_points]
        # print(extracted_points)
        for i in range(len(extracted_points)):
            if extracted_points[i][0] > maxx :
                maxx = extracted_points[i][0]
                maxx_y = extracted_points[i][1]
            if  extracted_points[i][0] < minx:
                minx = extracted_points[i][0]
                minx_y = extracted_points[i][1]

        mid_coordinate = (int((minx + maxx) / 2), int(((minx_y + maxx_y) / 2)))
        return mid_coordinate

def getDistance(midPoint, laneNo):

    if midPoint != None:
        if laneNo == '5':
            n = 144*midPoint[1]*-1 - 35*midPoint[0] + 225888
            d = math.sqrt(144*144+35*35)
            distance = int(n/d)
            return distance

        elif laneNo == '4':
            n = 205*midPoint[1]*-1 - 18*midPoint[0] + 268208
            d = math.sqrt(18*18+205*205)
            distance = int(n/d)
            return distance

        elif laneNo == '3':
            n = 203*midPoint[1]*-1 + 2*midPoint[0] + 242121
            d = math.sqrt(203*203+2*2)
            distance = int(n/d)
            return distance

        elif laneNo == '2':
            n = 149*midPoint[1]*-1 + 19*midPoint[0] + 159271
            d = math.sqrt(149*149+19*19)
            distance = int(n/d)
            return distance
        else:
            return None

    # return None
