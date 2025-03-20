import cv2

image=cv2.imread('maresca.jpg')

B,G,R=cv2.split(image)


cv2.imshow("Original", image)

cv2.waitKey(0)


cv2.imshow("white", B)

cv2.waitKey(0)



cv2.imshow("white", G)

cv2.waitKey(0)



cv2.imshow("yellow", R)

cv2.waitKey(0)