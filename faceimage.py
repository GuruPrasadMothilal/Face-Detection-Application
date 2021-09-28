import cv2
#traineddataset
traineddataset=cv2.CascadeClassifier("xml doc.xml")
import tkinter as tk
from tkinter import filedialog
def sampletest():
    root=tk.Tk()
    root.withdraw()
    filepath=filedialog.askopenfilename()
    return filepath

#read a image
img=cv2.imread(sampletest())

#convert into grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=traineddataset.detectMultiScale(gray)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('guru',img)
#cv2.imshow('gray',gray)

cv2.waitKey()
