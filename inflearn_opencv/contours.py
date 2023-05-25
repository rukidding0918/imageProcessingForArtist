import cv2

file_name = "./sungmi/2019/20211105_114438.jpg"

img = cv2.imread(file_name)
img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

target_img = img.copy() # copy를 안 하면 원본을 바꾸기 때문에 꼭 복사해야 함!!!
# 흑백으로 먼저 바꾼 다음에 작업
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)

# 윤곽선 검출
### contours는 윤곽선 정보, hierachy는 윤곽선의 계층 구조
### params: image, contour retrieval mode(윤곽선 찾는 모드), contour approximation method(윤곽선을 찾을 때 사용하는 근사치 방법)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 윤곽선 찾는 모드의 옵션
# cv2.RETR_EXTERNAL: 가장 바깥쪽 윤곽선만 검출
# cv2.RETR_LIST: 모든 윤곽선을 검출하나, 계층 구조는 만들지 않음
# cv2.RETR_CCOMP: 모든 윤곽선을 검출하고, 2단계 계층 구조를 만듦
# cv2.RETR_TREE: 모든 윤곽선을 검출하고, 전체 계층 구조를 만듦
# 윤곽선을 찾을 때 사용하는 근사치 방법의 옵션
# cv2.CHAIN_APPROX_SIMPLE: 수직, 수평, 대각선 방향의 점은 모두 버리고 끝점만 남김
# cv2.CHAIN_APPROX_NONE: 모든 점을 윤곽선으로 저장



# 윤곽선 그리기
# params: image, contours, contourIdx(그릴 윤곽선의 인덱스. -1로 하면 모든 윤곽선을 다 그림), color, thickness
height, width = img.shape[1::-1]
area = height * width
COLOR = (0, 255, 0)
THICKNESS = 2
for cnt in contours:
    # 면적 - 면적이 너무 작거(30%이하)나 반대로 너무 큰 것(99%) 제거
    if area * 0.99 > cv2.contourArea(cnt) > area *0.3:
        cv2.drawContours(target_img, [cnt], -1, COLOR, THICKNESS)


cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("otsu", otsu)



while True:
    # cv2.imshow("target_img", target_img)
    cv2.imshow('target', target_img)

    if cv2.waitKey(1) == ord('q'):
        break

    if cv2.waitKey(1) == ord('s'):
        file_split = file_name.rsplit('.', maxsplit=1)
        result_file_name = file_split[0] + '_result' + file_split[1]
        cv2.imwrite('./sungmi/2019/20211105_114438_result.jpg', target_img)
        break

# print(f'contours 개수: {len(contours)}')
# print(f'hierarchy: {hierarchy}')

# cv2.waitKey(0)
cv2.destroyAllWindows()