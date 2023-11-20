import numpy as np
import cv2

img = cv2.imread('/home/swaraj/Downloads/shapes.png')
Blur=cv2.GaussianBlur(img, (1,1), 0) 
# cv2.imshow("Blur",Blur)
# cv2.waitKey(0) 
Gray=cv2.cvtColor(Blur,cv2.COLOR_BGR2GRAY) 
# cv2.imshow("Gray",Gray)
# cv2.waitKey(0) 
ret,thresh=cv2.threshold(Gray,150,250,1) 
# cv2.imshow('thresh', thresh)
# cv2.waitKey(0)
kernel = np.ones((1,1)) 
Dilate=cv2.dilate(thresh, kernel, iterations=2) 
# cv2.imshow('Dilate', Dilate)
# cv2.waitKey(0)
contours , hierarchy = cv2.findContours(Dilate.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True) 
    cv2.drawContours(img, [approx], 0, (20, 20, 20), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    x, y , w, h = cv2.boundingRect(approx) 
    cv2.rectangle(img, (x, y), (x + w, y + h), (250, 0, 0), 1)
	
 
 
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy =0, 0
			# finding center point of shape

			# Draw a point at the center of the shape
    cv2.circle(img, (cx, cy), 2	, (250, 0, 0), -4)
    
    
    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1) ) 
    elif len(approx) == 4:
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio > 0.90 and aspectRatio < 1.2:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1)) 
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 0.6, 1))
    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1))
    elif len(approx) == 6 :
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1))
    elif len(approx) == 8 :
        cv2.putText(img, "octagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1))
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 1))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()