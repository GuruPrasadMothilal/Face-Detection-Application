import cv2
traineddataset=cv2.CascadeClassifier('xml doc.xml')
video=cv2.VideoCapture(0)
while True:
    success, frame = video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = traineddataset.detectMultiScale(gray_image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

        cv2.imshow('video', frame)
        quit=cv2.waitKey(1)
        if quit==113:
            break
    else:
        print("video completeed")
        break
