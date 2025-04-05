# Canny Edge detection

import cv2

# Load the image
image = cv2.imread('madueke.jpg', cv2.IMREAD_GRAYSCALE)

# Resize image
image = cv2.resize(image, (400, 400))

# Perform Canny edge detection
edges = cv2.Canny(image, 100, 200)  # Adjust the threshold values as needed

# Display the original image and the detected edges
cv2.imshow('Original', image)
cv2.imshow('Edges', edges)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
