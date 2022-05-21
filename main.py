import cv2

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('frontalface.xml')

while True:

    sucess, image = cap.read()

    face = faceCascade.detectMultiScale(image,1.2,4)

    for (x,y,w,h) in face:

        ROI = image[y:y+h, x:x+w]

        blur = cv2.GaussianBlur(ROI, (91,91), 0)

        image[y:y+h, x:x+w] = blur

    if face == ():

        cv2.putText(image, 'reesayez Pas de visage detecter',(20,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))

    cv2.imshow('Master Lipakumu real time Face Blur', image)

    if cv2.waitKey(1) & 0xff == ord('q') :

        break



cap.release()
cv2.destroyAllWindows()
