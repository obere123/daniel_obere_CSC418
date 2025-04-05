def Sobel_edge_detection():
    # Canny Edge detection

    import cv2

    # Load the image
    image = cv2.imread('img/chudi.jpg', cv2.IMREAD_GRAYSCALE)

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

def Prewitt_Edge_Detection():
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

def Robert_Edge_Detection():
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


def Laplacian_Edge_Detection():
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

def Canny_edge_detection():
    # Canny Edge detection

    import cv2
    import pandas

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

import pandas
data={
    "Name":["Sobel Edge","Prewitt Edge", "Robert Edge", "Laplacian Edge", "Canny edge"]
}

df=pandas.DataFrame(data, index=[1,2,3,4,5])
df.index.name="S/N"


print(df)


userinput=input("Enter in detection you want given the number")

if userinput=="1":
    Sobel_edge_detection()

elif userinput=="2":
    Prewitt_Edge_Detection()
elif userinput=="3":
    Robert_Edge_Detection()
elif userinput=="4":
    Laplacian_Edge_Detection()
elif userinput==5:
    Canny_edge_detection()
else:
    print("Invalid Input")






