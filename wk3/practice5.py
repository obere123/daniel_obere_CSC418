import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('caicedo.jpg', 0)
rows, cols = img.shape

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img)

M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

plt.subplot(1, 2, 2)
plt.title("Sheared Image")
plt.imshow(sheared_img)
plt.show()

cv.imshow('img', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()
