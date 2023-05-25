import cv2
import numpy as np


def empty(pos):
    pass


file_name = "./sungmi/2019/20211105_114438.jpg"

img = cv2.imread(file_name)
img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

# https://bkshin.tistory.com/entry/OpenCV-15-%EB%A6%AC%EB%A7%A4%ED%95%91Remapping-%EC%98%A4%EB%AA%A9%EB%B3%BC%EB%A1%9D-%EB%A0%8C%EC%A6%88-%EC%99%9C%EA%B3%A1Lens-Distortion-%EB%B0%A9%EC%82%AC-%EC%99%9C%EA%B3%A1Radial-Distortion
rows, cols = img.shape[:2]
mapy, mapx = np.indices((rows, cols),dtype=np.float32)
mapx = 2*mapx/(cols-1)-1
mapy = 2*mapy/(rows-1)-1

r, theta = cv2.cartToPolar(mapx, mapy)

name = "distorted"
cv2.namedWindow(name)
cv2.createTrackbar('왜곡 계수', name, 0, 1000, empty)

while True:
    k = cv2.getTrackbarPos('왜곡 계수', name)
    k1 = 0.5 * k / 1000
    k2 = 0.2 * k / 1000
    k3 = 0.0 * k / 1000

    ru = r*(1 + k1*(r**2) + k2*(r**4) + k3*(r**6))
    mapx, mapy = cv2.polarToCart(ru, theta)
    mapx = ((mapx + 1)*cols-1)/2
    mapy = ((mapy + 1)*rows-1)/2
    distored = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    cv2.imshow('distorted', distored)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('distorted.jpg', distored)
        break

cv2.destroyAllWindows()
