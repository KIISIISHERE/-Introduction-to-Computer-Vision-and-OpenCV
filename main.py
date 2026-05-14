import cv2
#load the image
img=cv2.imread("image.png")
#shw the image that has loaded
cv2.imshow("Sample Image",img)
#wait until the user presses a key
key=cv2.waitKey(1) &0xFF
if key==ord('q'):
    cv2.destroyAllWindows()