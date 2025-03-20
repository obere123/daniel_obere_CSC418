# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('palmerboy.jpg')

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

# Scale the image by a factor of 2 along both axes
scaled_image = cv2.resize(image, None, fx=2, fy=2)

# Save the scaled image
#cv2.imwrite('img/Scaled.jpg', scaled_image)

# Plot the scaled image
plt.subplot(1, 2, 2)
plt.title("Scaled")
plt.imshow(scaled_image)

# Show both images
plt.show()