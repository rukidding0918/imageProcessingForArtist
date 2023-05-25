import cv2


file_name = "./sungmi/2019/20211105_114438.jpg"

img = cv2.imread(file_name)
img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

# 경계선 검출
# Canny Edge Detection
# 대상이미지 minVal(하위임계값) maxVal(상위임계값)

def empty(pos):
    pass


name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar('minVal', name, 0, 255, empty)
cv2.createTrackbar('maxVal', name, 0, 255, empty)

while True:
    minVal = cv2.getTrackbarPos('minVal', name)
    maxVal = cv2.getTrackbarPos('maxVal', name)
    canny = cv2.Canny(img, minVal, maxVal)
    cv2.imshow('img', img)
    cv2.imshow(name, canny)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()