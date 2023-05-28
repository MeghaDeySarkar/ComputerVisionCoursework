import cv2
import numpy as np

img = cv2.imread('Lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting image to grayscale

rows,cols = img.shape[0],img.shape[1]

img_new7 = np.zeros([rows,cols]) #initializing new image

# implementaing 7*7 average filtering
kernal = np.array([1,1,1,1,1,1,1])*(1/7) #initializing kernal
for i in range(rows):
    for j in range(cols-6):
        img_new7[i][j+3] = (gray[i][j]*kernal[0])+(gray[i][j+1]*kernal[1])+(gray[i][j+2]*kernal[2])+(gray[i][j+3]*kernal[3])+(gray[i][j+4]*kernal[4])+(gray[i][j+5]*kernal[5])+(gray[i][j+6]*kernal[6])
for i in range(cols):
    for j in range(rows-6):
        img_new7[j+3][i] = (img_new7[j][i]*kernal[0])+(img_new7[j+1][i]*kernal[1])+(img_new7[j+2][i]*kernal[2])+(img_new7[j+3][i]*kernal[3])+(img_new7[j+4][i]*kernal[4])+(img_new7[j+5][i]*kernal[5])+(img_new7[j+6][i]*kernal[6])

img_new7 = img_new7.astype(np.uint8)
print(img_new7[2])
while(True):
    cv2.imshow("Original Image",img)
    cv2.imshow("Grayscale Image",gray)
    cv2.imshow("7*7 filter",img_new7)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()