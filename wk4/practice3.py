# Robert Edge Detection

import cv2
import numpy as np

# Load the image
image = cv2.imread('madueke.jpg', cv2.IMREAD_GRAYSCALE)

# Perform Gaussian Blur
image = cv2.GaussianBlur(image, (5, 5), 0)

# Define Robert kernels
kernel_x = np.array([[1, 0],
                     [0, -1]])

kernel_y = np.array([[0, 1],
                     [-1, 0]])

# Apply Robert edge detection
robert_x = cv2.filter2D(image, -1, kernel_x)
robert_y = cv2.filter2D(image, -1, kernel_y)

# Combine the gradient images
robert_combined = np.sqrt(np.square(robert_x) + np.square(robert_y))

# Display the original image and the Robert edges
cv2.imshow('Original', image)
cv2.imshow('Robert Edges', np.uint8(robert_combined))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
