# pip install opencv-python opencv-contrib-python

import cv2

#image path

imagepath = "img/4.jpg"

#importing cascade

casPath = "caspathimage.xml"

#Create the haar cascade

faceCascade = cv2.CascadeClassifier(casPath)

#read image into cv2

image = cv2.imread(imagepath)

#grayscaling image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 1,
    minSize = (10 , 10), 
    flags = cv2.CASCADE_SCALE_IMAGE
)

# Draw Rectangle around faces

for (x , y , w , h) in faces:
    cv2.rectangle(image, (x , y), (x + w , y + h), (255, 0 , 0), 2)

print(len(faces))
cv2.imwrite("detected/Faces.jpg", image)

#Only for App IDE
# cv2.imshow("Faces I detected", image)
# cv2.waitKey(0)

