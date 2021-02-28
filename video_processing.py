import cv2 as cv

video = cv.VideoCapture("Cars.mp4")
findCar = cv.CascadeClassifier("cars.xml")

while True:
    ret, kare = video.read()
    gray = cv.cvtColor(kare, cv.COLOR_BGR2GRAY)
    cars = findCar.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in cars:
        cv.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),4)
        cv.imshow("Video", kare)
        if cv.waitKey(1) & 0xFF == ord("Q"):
            break

video.release()
cv.destroyAllWindows()