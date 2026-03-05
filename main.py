import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

testGridsize = 8
testCliplimit = 4
count1 = 180
count2 = 80

# Create CLAHE once
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(testGridsize, testGridsize))

def update_values(*args):
    global testGridsize, testCliplimit, count1, count2, clahe

    testGridsize = gridsize_scale.get()
    testCliplimit = cliplimit_scale.get()
    count1 = count1_scale.get()
    count2 = count2_scale.get()

    if testGridsize < 1:
        testGridsize = 1
    if testCliplimit < 1:
        testCliplimit = 1

    # recreate CLAHE only when sliders change
    clahe = cv2.createCLAHE(
        clipLimit=testCliplimit * 0.5,
        tileGridSize=(testGridsize, testGridsize)
    )

def update_frame():
    ret, frame = cam.read()

    if ret:

        # Fast resize
        frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cl1 = clahe.apply(gray)

        clamp = np.uint8(np.interp(cl1, [count2, count1], [0,255]))

        equ = clahe.apply(clamp)

        img = Image.fromarray(equ)
        imgtk = ImageTk.PhotoImage(img)

        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)

    lmain.after(1, update_frame)

root = Tk()
root.title("Video CLAHE Filter")

gridsize_scale = Scale(root, from_=1, to=24, orient=HORIZONTAL, label="Grid Size")
gridsize_scale.set(testGridsize)
gridsize_scale.pack()

cliplimit_scale = Scale(root, from_=1, to=40, orient=HORIZONTAL, label="Clip Limit")
cliplimit_scale.set(testCliplimit)
cliplimit_scale.pack()

count1_scale = Scale(root, from_=180, to=500, orient=HORIZONTAL, label="Count1")
count1_scale.set(count1)
count1_scale.pack()

count2_scale = Scale(root, from_=80, to=500, orient=HORIZONTAL, label="Count2")
count2_scale.set(count2)
count2_scale.pack()

lmain = Label(root)
lmain.pack()

gridsize_scale.bind("<Motion>", update_values)
cliplimit_scale.bind("<Motion>", update_values)
count1_scale.bind("<Motion>", update_values)
count2_scale.bind("<Motion>", update_values)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_BUFFERSIZE,1)

update_frame()

root.mainloop()

cam.release()
cv2.destroyAllWindows()
