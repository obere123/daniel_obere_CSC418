import cv2

image1=cv2.imread("maresca.jpg")
image2=cv2.imread("peter.jpg")

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