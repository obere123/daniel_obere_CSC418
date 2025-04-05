# Sobel edge detection

import cv2
import numpy as np

# Load the image
image = cv2.imread('madueke.jpg', cv2.IMREAD_GRAYSCALE)

# Resize image
image = cv2.resize(image, (500, 400))

# Apply Sobel edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the gradient images
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Display the original image and the Sobel edges
cv2.imshow('Original', image)
cv2.imshow('Sobel Edges', np.uint8(sobel_combined))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
