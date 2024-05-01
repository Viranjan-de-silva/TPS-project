import cv2

line_color = (250, 0, 50)
thickness = 6

#===============================================LANE05 Allignment line =================================================
lane5_start = (1560,555)
lane5_end = (1675,550)
lane5_start2 = (1776,1137)
lane5_end2 = (1920,1102)
alignment_line_color = (0, 255, 0)

#===============================================LANE02 Allignment line =================================================
lane2_start = (895,605)
lane2_end = (1029,587)
lane2_start2 = (722,1161)
lane2_end2 = (871,1180)

#===============================================LANE04 Allignment line =================================================
lane4_start = (1342,566)
lane4_end = (1466,550)
lane4_start2 = (1416,1184)
lane4_end2 = (1621,1166)

#===============================================LANE03 Allignment line =================================================
lane3_start = (1109,593)
lane3_end = (1240,580)
lane3_start2 = (1044,1203)
lane3_end2 = (1247,1205)

#===========================================================ROIs++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lane1 = ((890,530),(1100,530),(907,1440),(515,1440))
lane2 = ((1100,530),(1265,530),(1310,1440),(907,1440))
lane3 = ((1265,530),(1465,530),(1775,1440),(1310,1440))
lane4 = ((1465,530),(1685,530),(2160,1440),(1775,1440))

#horizontal_line(HL)
HLstart_point = (890,530)
HLend_point = (1685,530)

#=================Lines===============
L1start = (890,530)
L1end = (515,1440)

L2start = (1100,530)
L2end = (907,1440)

L3start = (1265,530)
L3end = (1310,1440)

L4start = (1465,530)
L4end = (1775,1440)

L5start = (1685,530)
L5end = (2160,1440)

def drawTruckLanes(frame):
    # ----------------------Truck lane lines---------------------------------------
    cv2.line(frame, HLstart_point, HLend_point, line_color, thickness)
    cv2.line(frame, L1start, L1end, line_color, thickness)
    cv2.line(frame, L2start, L2end, line_color, thickness)
    cv2.line(frame, L3start, L3end, line_color, thickness)
    cv2.line(frame, L4start, L4end, line_color, thickness)
    cv2.line(frame, L5start, L5end, line_color, thickness)

    # --------------------Alignment lines----------------------------
    cv2.line(frame, lane5_start, lane5_end, alignment_line_color, thickness)
    cv2.line(frame, lane4_start, lane4_end, alignment_line_color, thickness)
    cv2.line(frame, lane2_start, lane2_end, alignment_line_color, thickness)
    cv2.line(frame, lane3_start, lane3_end, alignment_line_color, thickness)

    cv2.line(frame, lane5_start2, lane5_end2, alignment_line_color, thickness)
    cv2.line(frame, lane4_start2, lane4_end2, alignment_line_color, thickness)
    cv2.line(frame, lane2_start2, lane2_end2, alignment_line_color, thickness)
    cv2.line(frame, lane3_start2, lane3_end2, alignment_line_color, thickness)

