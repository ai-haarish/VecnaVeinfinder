import cv2
import numpy as np
from skimage.filters import frangi
from skimage.morphology import skeletonize

# open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # resize for speed
    frame = cv2.resize(frame,(640,480))

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ---- Flat-field illumination correction ----
    background = cv2.GaussianBlur(gray,(51,51),0)
    flat = cv2.divide(gray, background, scale=255)

    # ---- CLAHE contrast enhancement ----
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(flat)

    # ---- Noise reduction ----
    smooth = cv2.GaussianBlur(enhanced,(5,5),0)

    # ---- Frangi vessel detection ----
    vessels = frangi(smooth, scale_range=(1,6), scale_step=1)

    # normalize
    vessels_norm = cv2.normalize(vessels,None,0,255,cv2.NORM_MINMAX)
    vessels_uint8 = vessels_norm.astype('uint8')

    # ---- Adaptive threshold ----
    binary = cv2.adaptiveThreshold(
        vessels_uint8,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        15,
        -2
    )

    # ---- Morphological cleanup ----
    kernel = np.ones((3,3),np.uint8)
    clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)

    # ---- Skeletonization ----
    skeleton = skeletonize(clean//255)
    skeleton = (skeleton*255).astype(np.uint8)

    # ---- Overlay veins on original image ----
    color = frame.copy()
    color[skeleton==255] = [0,255,0]

    # display windows
    cv2.imshow("Original",frame)
    cv2.imshow("Enhanced",enhanced)
    cv2.imshow("Vessels",vessels_uint8)
    cv2.imshow("Vein Lines",skeleton)
    cv2.imshow("Overlay",color)

    # press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()