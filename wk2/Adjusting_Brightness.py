# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('maresca.jpg')

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

# Adjust the brightness and contrast
brightness = 5
contrast = 1.5
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

# Save the image
cv2.imwrite('img/contrast_image.jpg', image2)

# Plot the contrast image
plt.subplot(1, 2, 2)
plt.title("Brightness & Contrast")
plt.imshow(image2)

# Show the images
plt.show()