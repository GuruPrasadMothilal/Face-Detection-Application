from tkinter import *
root=Tk()
root.geometry('13333x13343')
root.title("Guru Prasad Mothilal")
root.configure(background=('blue'))
label=Label(root,text="Welcome to Face Detection Application",fg="black",bg='red',font='Calibri 32 bold italic')
label.pack()
def webcamfn():
    import facewebcam
def videofn():
    import facevideo
def imagefn():
    import faceimage
button_imagefn=Button(root,text="image",padx=11,pady=11,command=imagefn,fg="black",bg="white")
button_imagefn.pack()

button_videofn=Button(root,text="video",padx=11,pady=11,command=videofn,fg="black",bg="white")
button_videofn.pack()
button_webcamfn=Button(root,text="webcam",padx=11,pady=11,command=webcamfn,fg="black",bg="white")
button_webcamfn.pack()
button_quit=Button(root,text="quit",padx=11,pady=11,command=root.destroy,fg="black",bg="white")
button_quit.pack()

root.mainloop()
