# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('palmerboy.jpg')

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")

plt.imshow(image)

# Inverse by subtracting from 255
inverse_image = 255 - image

# Save the inverted image
#cv2.imwrite('img/inverse_image.jpg', inverse_image)

# Plot the inverted image
plt.subplot(1, 2, 2)
plt.title("Inverse color")
plt.imshow(inverse_image)

# Show both images
plt.show()