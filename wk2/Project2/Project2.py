import cv2
import matplotlib.pyplot as plt
import numpy as np 

dumebi_image=cv2.imread("./dumebi.jpeg")
bimpe_image=cv2.imread("./bimpe.jpeg")
ada_image=cv2.imread("./ada.jpeg")
chima_image=cv2.imread("./chima.jpeg")
clement_image=cv2.imread("./clement.jpeg")
esonu_image=cv2.imread("./esonu.jpeg")
love_image=cv2.imread("./love.jpeg")
maryam_image=cv2.imread("./maryam.jpeg")
miracle_image=cv2.imread("./miracle.jpeg")
oyinda_image=cv2.imread("./oyinda.jpeg")
tomi_image=cv2.imread("./tomi.jpeg")

lyst=["Dumebi", "Bimpe", "Ada","Chima", "Clement", "Esonu", "Love","Maryam", "Miracle", "Oyinda", "Tomi"]

picture_dict={
"Dumebi": dumebi_image,
"Bimpe": bimpe_image,
"Ada": ada_image,
"Chima": chima_image,
"Clement": clement_image,
"Esonu": esonu_image,
"Love":love_image,
"Maryam": maryam_image,
"Miracle": miracle_image,
"Oyinda": oyinda_image,
"Tomi": tomi_image
}

random_number=2112061254
matric_dict={}

for i in lyst:
    matric_dict[i]=random_number
    random_number+=1
print(matric_dict)

def InverseTransform(imagex):
    image = imagex

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


def ImageScaling(imagex):
    # Load the image
    image = imagex

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



def Removing_Noise(imagex):

     # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(imagex)

    # Remove noise using a median filter
    filtered_image = cv2.medianBlur(imagex, 15)

    # Save the filtered image
    #cv2.imwrite('img/Median-Blur.jpg', filtered_image)

    # Plot the blurred image
    plt.subplot(1, 2, 2)
    plt.title("Median Blur")
    plt.imshow(filtered_image)

    # Show both images
    plt.show()


def Adjusting_Brightness(imagex):
    # Load the image
    image = imagex

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

def AddingImages(imagex):
    #import cv2

    image1=cv2.imread(imagex)
    image2=cv2.imread(imagex)

    #resize images

    image1 = cv2.resize(image1, (500,400))
    image2 = cv2.resize(image2, (500,400))


    addImage=cv2.addWeighted(image1, 0.5, image2, 0.6, 0)
 
    # cv2.imshow('Image 1', image2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # addImage=cv2.addWeighted(image1,0.5,image2,0.6,0)


    # # sub= cv2.subtractImage(image1,image2)

    cv2.imshow("Weighted image", addImage)


    # #Deallocate any associated memmory usage
    if cv2.waitKey(0) & 0xff==27:
        cv2.destroyAllWindows()

def SharpeningImages(imagex):
    image = imagex

    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)

    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])

    # Sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Save the image
    cv2.imwrite('img/sharpened_image.jpg', sharpened_image)

    # Plot the sharpened image
    plt.subplot(1, 2, 2)
    plt.title("Sharpening")
    plt.imshow(sharpened_image)

    # Show both images
    plt.show()
Removing_Noise(love_image)
# """
# nameinput=input("Enter in your name  ")
# if nameinput not in lyst:
#     print("Name does not exist")
# else:
#     matric_no=input("Enter in matric no")
#     if matric_dict[nameinput]== matric_no:
#         lystt=["Removing Noise", "Image Scaling", "Inverse Transformation", "Sharpening Images", "Adding Images", "Adjusting Brightness"]
#         inputt=input(f"Enter in function you want from the following  {lystt}")"
#         """