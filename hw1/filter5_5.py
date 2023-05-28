import cv2
import numpy as np

img = cv2.imread('Lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting image to grayscale

rows,cols = img.shape[0],img.shape[1]

img_new5 = np.zeros([rows,cols]) #initializing new image

# implementaing 5*5 average filtering
kernal = np.array([1,1,1,1,1])*(1/5) #initializing kernal
for i in range(rows):
    for j in range(cols-4):
        img_new5[i][j+2] = (gray[i][j]*kernal[0])+(gray[i][j+1]*kernal[1])+(gray[i][j+2]*kernal[2])+(gray[i][j+3]*kernal[3])+(gray[i][j+4]*kernal[4])
for i in range(cols):
    for j in range(rows-4):
        img_new5[j+2][i] = (img_new5[j][i]*kernal[0])+(img_new5[j+1][i]*kernal[1])+(img_new5[j+2][i]*kernal[2])+(img_new5[j+3][i]*kernal[3])+(img_new5[j+4][i]*kernal[4])

img_new5 = img_new5.astype(np.uint8)

print(img_new5[2])

while(True):
    cv2.imshow("Original Image",img)
    cv2.imshow("Grayscale Image",gray)
    cv2.imshow("5*5 filter",img_new5)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()