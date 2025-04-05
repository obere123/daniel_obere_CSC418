# Laplacian Edge Detection

import cv2

# Load the image
image = cv2.imread('madueke.jpg', cv2.IMREAD_GRAYSCALE)

# Resize image
image = cv2.resize(image, (400, 400))

# Perform Gaussian Blur
# image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Laplacian edge detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the output to an 8-bit image
laplacian = cv2.convertScaleAbs(laplacian)

# Display the original image and the Laplacian edges
cv2.imshow('Original', image)
cv2.imshow('Laplacian Edges', laplacian)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
