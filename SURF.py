import cv2
img = cv2.imread('ummmet.png',0)
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
print(len(kp))