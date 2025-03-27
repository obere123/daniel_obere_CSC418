import numpy as np
import matplotlib.pyplot as plt

import cv2 as cv


img = cv.imread('caicedo.jpg',0)

rows,col=img.shape

#Plot the original shape

plt.subplot(1,2,1)

plt.title("Original")
plt.imshow(img)


M=np.float32([[1,0,100],[0,1,50]])

trans1=cv.warpAffine(img,M,(col,rows))

#Plot the translated image

plt.subplot(1,2,2)

plt.title("Translated image")

plt.imshow(trans1)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

