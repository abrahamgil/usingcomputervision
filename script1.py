import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized" + image,re)

"""
img=cv2.imread("galaxy.jpg",0) #0 gives you grayimage, 1 gives you color

print(type(img)) #shows you its an array
print(img)
print(img.shape) #gives you resolution
print(img.ndim) #gives you dimensions

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resizes image before displaying values are pixel size resizes based on doing averages between colors
cv2.imshow("Galaxy", resized_image) #shows images in window
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(0) #timer before window closes. 0 allows user to close window with any button. Values in milliseconds when you do ex. 2000
cv2.destroyAllWindows() #closes all windows
"""