import cv2
a=cv2.CascadeClassifier('face detection.xml')
img=cv2.imread('faces.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
b=a.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in b:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('face detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()