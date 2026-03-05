import cv2
import numpy as np
from numpy.linalg import eigh, eig
# for installing the camera
cap =cv2.VideoCapture(0)
# for the full sized screen bitch
cv2.namedWindow("Vienfinder", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Vienfinder", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


# for the math def get_eigen_viens(frame):
def get_eigen_veins(frame):
   #  gray scale conversionku
   grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray, (5,5),0).astype(np.float32)
   dxx = cv2.Sobel(blur, cv2.CV_32F, 1,0, ksize=3)
   dyy = cv2.Sobel(blur, cv2.CV_32F, 0,1, ksize=3)
   dxy = cv2.Sobel(blur, cv2.CV_32F, 0,1, ksize=3)    
   #enna peru vankarathu nu theriyeala 
   kd = dxx + dyy
   sqr = dxx*dyy-dxy**2
   dist = np.sprt(np.maximum(kd**2 - 4*spr,0))
   lamba_max = (kd + spr)/2.0
   res =cv2.normalize(lamda_max, None,0,255, cv2.NORM_MINMAX).astype(np.unit8)
   return cv2.applyColorMap(res, cv2.COLORMAP_BONE)
while True:
  ret,frame = cap.read()
  if not ret: break
  vein_visula = get_eigen_viens(frame)
  cv2.imshow("viens", vein_visula)
  if cv2.waitkey(1) & 0xFF --ord('q'):
     break
cap.release()
cv2.destroyAllWindows()


