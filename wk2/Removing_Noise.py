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

# Remove noise using a median filter
filtered_image = cv2.medianBlur(image, 15)

# Save the filtered image
#cv2.imwrite('img/Median-Blur.jpg', filtered_image)

# Plot the blurred image
plt.subplot(1, 2, 2)
plt.title("Median Blur")
plt.imshow(filtered_image)

# Show both images
plt.show()