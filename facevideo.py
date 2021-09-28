import cv2
import tkinter as tk
from tkinter import filedialog
def sampletest():
    root=tk.Tk()
    root.withdraw()
    filepath=filedialog.askopenfilename()
    return filepath

traineddataset=cv2.CascadeClassifier(r"C:\Users\GURU\PycharmProjects\!st project\xml doc.xml")
video=cv2.VideoCapture(sampletest())
while True:
    success, frame = video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = traineddataset.detectMultiScale(gray_image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video', frame)
        key=cv2.waitKey(1)
        if key==113:
            break

    else:
        print("video completed")
        break
