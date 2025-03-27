import numpy as np
import matplotlib.pyplot as plt

import cv2 as cv

img=cv.imread('caicedo.jpg',0)

#Plot the original image
plt.subplot(1,2,1)
plt.title("Image")
plt.imshow(img)

rows,col=img.shape

M=np.float32([[1,0,0],[0,-1,rows],[0,0,1]])
reflected_img=cv.warpPerspective(img,M, (int(col),int(rows)))

#plot the refelcted img


plt.subplot(1,2,2)
plt.title("Refelected Image")
plt.imshow(reflected_img)
cv.imshow("reflc",reflected_img)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi")