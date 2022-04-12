import cv2
filePath = 'KRAB_Pink-desktop.jpg'
image = cv2.imread(filePath, 1)
cv2.imshow("KRAB", image)
cv2.waitkey(0)
cv2.destroyAllWindows()
