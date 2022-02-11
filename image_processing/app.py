import cv2

#0 means gray scene
#1 means color scene
#-1 means color image scene and also alfa channel = transparency
img = cv2.imread("../files/galaxy.jpg", 0)

print(dir(cv2))
print(type(img))
print(img.shape)
print(img.ndim)
resized_img=cv2.resize(img, (1000,500))
cv2.imshow("GALAXY", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
