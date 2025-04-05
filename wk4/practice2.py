# Prewitt Edge Detection

import cv2
import numpy as np

# Load the image
image = cv2.imread('madueke.jpg', cv2.IMREAD_GRAYSCALE)

# Resize image
image = cv2.resize(image, (500, 400))

# Define Prewitt kernels
kernel_x = np.array([[-1, 0, 1], 
                      [-1, 0, 1], 
                      [-1, 0, 1]])

kernel_y = np.array([[-1, -1, -1], 
                      [0, 0, 0], 
                      [1, 1, 1]])

# Apply Prewitt edge detection
prewitt_x = cv2.filter2D(image, -1, kernel_x)
prewitt_y = cv2.filter2D(image, -1, kernel_y)

# Compute magnitude of gradients manually
prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

# Display the original image and the Prewitt edges
cv2.imshow('Original', image)
cv2.imshow('Prewitt Edges', np.uint8(prewitt_combined))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
