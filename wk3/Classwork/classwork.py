import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


contemporary1='Contemporary/contemporary.jpg'
contemporary2='Contemporary/contemporary1.jpg'
contemporary3='Contemporary/contemporary2.jpg'
modern1='Modern/modern1.jpg'
modern2='Modern/modern2.jpg'
modern3='Modern/modern3.jpg'
traditional1='Traditional/traditional1.jpg'
traditional2='Traditional/traditional2.jpg'
traditional3='Traditional/traditional1.jpg'

ContemporaryList=[contemporary1,contemporary2,contemporary3]
ModernList=[modern1,modern2,modern3]
TraditionalList=[traditional1,traditional2,traditional3]

#Start of week 2


#End of week 2




def Translation(ima):
    img = cv.imread(ima,0)

    rows,col=img.shape

#Plot the original shape

    plt.subplot(1,2,1)

    plt.title("Original")
    plt.imshow(img)


    M=np.float32([[1,0,100],[0,1,50]])

    trans1=cv.warpAffine(img,M,(col,rows))

#Plot the translated image

    plt.subplot(1,2,2)

    plt.title("Translated image")

    plt.imshow(trans1)
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


def Reflection(ima):
           


   img=cv.imread(ima,0)

#Plot the original image
   plt.subplot(1,2,1)
   plt.title("Image")
   plt.imshow(img)

   rows,col=img.shape

   M=np.float32([[1,0,0],[0,-1,rows],[0,0,1]])
   reflected_img=cv.warpPerspective(img,M, (int(col),int(rows)))

#plot the refelcted img


   plt.subplot(1,2,2)
   plt.title("Refelected Image")
   plt.imshow(reflected_img)
   cv.imshow("reflc",reflected_img)
   cv.waitKey(0)
   cv.destroyAllWindows()
   print("Hi")
    

def Rotation(ima):
    img=cv.imread(ima,0)

    rows,cols=img.shape

    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(img)


    img_rotation=cv.warpAffine(img, cv.getRotationMatrix2D((cols/2,rows/2), 30,0.6),(cols,rows))

     #Plot the rotated image

    plt.subplot(1,2,2)
    plt.title("Rotated Image")
    plt.imshow(img_rotation)

    plt.show()
    cv.imshow('img',img_rotation)

    cv.waitKey(0)
    cv.destroyAllWindows()

def ImageCropping(ima):
    img = cv.imread(ima, 0)

    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(img)
    #plt.show()
    cropped_img = img[450:700, 200:5000]

    # Plot the cropped image
    plt.subplot(1, 2, 2)
    plt.title("Cropped Image")
    plt.imshow(cropped_img)
    plt.show()

    #cv.imwrite('cropped_out.jpg', cropped_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Sheared_Image_X(ima):
    img = cv.imread(ima, 0)
    rows, cols = img.shape

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(img)

    M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
    sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

    plt.subplot(1, 2, 2)
    plt.title("Sheared Image")
    plt.imshow(sheared_img)
    plt.show()

    cv.imshow('img', sheared_img)
    cv.waitKey(0)
    cv.destroyAllWindows()




def Sheared_Image_Y(ima):
    image = cv.imread(ima)

    cv.imshow('Original Image', image)
    cv.waitKey(0)

    # Gaussian Blur
    Gaussian = cv.GaussianBlur(image, (7, 7), 0)
    cv.imshow('Guassian Blurring', Gaussian)
    cv.waitKey(0)

    # Median Blur

    median = cv.medianBlur(image, 5)
    cv.imshow('Median Blurring', median)
    cv.waitKey(0)

    # Bilateral Blur
    bilateral = cv.bilateralFilter(image, 9, 75, 75)
    cv.imshow('Bilateral Blurring', bilateral)
    cv.waitKey(0)
    cv.destroyAllWindows()

def ImageBlurring(ima):
    image = cv.imread(ima)

    cv.imshow('Original Image', image)
    cv.waitKey(0)

    # Gaussian Blur
    Gaussian = cv.GaussianBlur(image, (7, 7), 0)
    cv.imshow('Guassian Blurring', Gaussian)
    cv.waitKey(0)

    # Median Blur

    median = cv.medianBlur(image, 5)
    cv.imshow('Median Blurring', median)
    cv.waitKey(0)

    # Bilateral Blur
    bilateral = cv.bilateralFilter(image, 9, 75, 75)
    cv.imshow('Bilateral Blurring', bilateral)
    cv.waitKey(0)
    cv.destroyAllWindows()









category=["Contemporary","Traditional", "Modern"]

email=input("Enter in your email   ")

age=int(input("Enter in your age   "))

if ('@' not in email) or (age <18):
    print("Invalid Input")

else:
    userpromt=input("Enter the category you want:  ")
    
    if userpromt==category[0]:
        for i in ContemporaryList:
            Translation(i)
            Rotation(i)
            ImageCropping(i)
            Sheared_Image_X(i)
            Sheared_Image_Y(i)
            ImageBlurring(i)
            Reflection(i)
    elif userpromt==category[1]:
          for i in TraditionalList:
                Translation(i)
                Rotation(i)
                ImageCropping(i)
                Sheared_Image_X(i)
                Sheared_Image_Y(i)
                ImageBlurring(i)
                Reflection(i)
    elif userpromt==category[2]:
        for i in ModernList:
            Translation(i)
            Rotation(i)
            ImageCropping(i)
            Sheared_Image_X(i)
            Sheared_Image_Y(i)
            ImageBlurring(i)
            Reflection(i)
    else:
        print("Not a valid category")





    
