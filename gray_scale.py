import cv2
import os


#Reading the image in gray scale mode
img=cv2.imread('fabrizio.jpg',0)

window_name="Fabrizio"

cv2.imshow(window_name,img)

cv2.waitKey(0)

cv2.destroyAllWindows()


