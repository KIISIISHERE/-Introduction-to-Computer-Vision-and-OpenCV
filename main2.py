import cv2
img=cv2.imread("image.png")
# Convert image to black and white
grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",grey_image)
key=cv2.waitKey(0)#wait indefinately
if key==ord("q"):
    cv2.destroyAllWindows()