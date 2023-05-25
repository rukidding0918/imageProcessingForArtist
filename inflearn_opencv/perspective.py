import cv2
import numpy as np


point_list = []
COLOR = (0, 0, 0)
THICKNESS = 1
RADIUS = 1
drawing = False

def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))

    if drawing:
        prev_point = None
        for point in point_list:
            cv2.circle(dst_img, point, RADIUS, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
        next_point = (x, y)
        if len(point_list) == 4:
            show_result()
            next_point = point_list[0]
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)

    cv2.imshow("img", dst_img)


def show_result():
    width, height = get_wh()
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow("result", result)
    cv2.imwrite("croped.jpg", result)

def get_wh():
    width1 = point_list[1][0] - point_list[0][0]
    width2 = point_list[2][0] - point_list[3][0]
    height1 = point_list[2][1] - point_list[1][1]
    height2 = point_list[3][1] - point_list[0][1]
    width = min(width1, width2)
    height = min(height1, height2)
    return width, height



# file_name = "./sungmi/2019/20211105_114438.jpg"
file_name = "distorted.jpg"

img = cv2.imread(file_name)
# img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)



cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()