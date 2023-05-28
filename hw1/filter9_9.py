import cv2
import numpy as np

img = cv2.imread('Lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting image to grayscale

rows,cols = img.shape[0],img.shape[1]

img_new9 = np.zeros([rows,cols]) #initializing new image

# implementaing 9*9 average filtering
kernal = np.array([1,1,1,1,1,1,1,1,1])*(1/9) #initializing kernal
for i in range(rows):
    for j in range(cols-8):
        img_new9[i][j+4] = (gray[i][j]*kernal[0])+(gray[i][j+1]*kernal[1])+(gray[i][j+2]*kernal[2])+(gray[i][j+3]*kernal[3])+(gray[i][j+4]*kernal[4])+(gray[i][j+5]*kernal[5])+(gray[i][j+6]*kernal[6])+(gray[i][j+7]*kernal[7])+(gray[i][j+8]*kernal[8])
for i in range(cols):
    for j in range(rows-8):
        img_new9[j+4][i] = (img_new9[j][i]*kernal[0])+(img_new9[j+1][i]*kernal[1])+(img_new9[j+2][i]*kernal[2])+(img_new9[j+3][i]*kernal[3])+(img_new9[j+4][i]*kernal[4])+(img_new9[j+5][i]*kernal[5])+(img_new9[j+6][i]*kernal[6])+(img_new9[j+7][i]*kernal[7])+(img_new9[j+8][i]*kernal[8])

img_new9 = img_new9.astype(np.uint8)
print(img_new9[2])
while(True):
    cv2.imshow("Original Image",img)
    cv2.imshow("Grayscale Image",gray)
    cv2.imshow("9*9 filter",img_new9)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()