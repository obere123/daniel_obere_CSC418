import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('caicedo.jpg', 0)

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img)
#plt.show()
cropped_img = img[450:700, 200:5000]

# Plot the cropped image
plt.subplot(1, 2, 2)
plt.title("Cropped Image")
plt.imshow(cropped_img)
plt.show()

#cv.imwrite('cropped_out.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
