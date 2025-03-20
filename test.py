import cv2

path='fabrizio.jpg'

#Reading an image in gray scale mode

window_name='VR Headset'

#Display image
img=cv2.imread(path,0)

cv2.imshow("Weighted",img)

cv2.waitKey(0)
