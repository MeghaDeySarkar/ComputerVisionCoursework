import cv2
import numpy as np
import copy
from scipy import signal

image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
after_agussian_blur = cv2.GaussianBlur(image,(3,3),cv2.BORDER_DEFAULT)

rows, columns = after_agussian_blur.shape

#Defining 5x5 sobel kernels
sobel_x = np.array([[2,2,4,2,2], [1,1,2,1,1], [0,0,0,0,0], [-1,-1,-2,-1,-1], [-2,-2,-4,-2,-2]])
sobel_y = np.array([[2,1,0,-1,-2], [2,1,0,-1,-2], [4,2,0,-2,-4], [2,1,0,-1,-2],[2,1,0,-1,-2]])

# # Convolve the image with the Sobel kernels
sobel_x_image = cv2.filter2D(after_agussian_blur, -1, sobel_x)/36
sobel_y_image = cv2.filter2D(after_agussian_blur, -1, sobel_y)/36


# Finding Sobel magnitute and orientation
sobel_image = np.sqrt(np.square(sobel_x_image) + np.square(sobel_y_image))
orientation = np.arctan2(sobel_x_image,sobel_y_image)

# Finding non-Maximum Supression
non_max_supressed_image = np.zeros([rows,columns])

degree = orientation * 180. / np.pi  # Converting Radians to Degrees
degree[degree < 0] += 180

for i in range(1,rows-1):
    for j in range(1,columns-1):
        
        temp1 = 255
        temp2 = 255
        
        #angle @ 0
        if (0 <= degree[i,j] < 22.5) or (157.5 <= degree[i,j] <= 180):
            temp1 = sobel_image[i, j+1]
            temp2 = sobel_image[i, j-1]
        #angle @ 45
        elif (22.5 <= degree[i,j] < 67.5):
            temp1 = sobel_image[i+1, j-1]
            temp2 = sobel_image[i-1, j+1]
        #angle @ 90
        elif (67.5 <= degree[i,j] < 112.5):
            temp1 = sobel_image[i+1, j]
            temp2 = sobel_image[i-1, j]
        #angle @ 135
        elif (112.5 <= degree[i,j] < 157.5):
            temp1 = sobel_image[i-1, j-1]
            temp2 = sobel_image[i+1, j+1]

        if (sobel_image[i,j] >= temp1) and (sobel_image[i,j] >= temp2):
            non_max_supressed_image[i,j] = sobel_image[i,j]
        else:
            non_max_supressed_image[i,j] = 0

# Threshold
thresholdRatio_min=0.1
thresholdRatio_max=0.3

threshold_max = non_max_supressed_image.max() * thresholdRatio_max
threshold_min = non_max_supressed_image.max() * thresholdRatio_min

threshold_image = np.zeros([rows,columns])

weak = np.int32(100)
strong = np.int32(255)

strong_i, strong_j = np.where(non_max_supressed_image >= threshold_max)
zeros_i, zeros_j = np.where(non_max_supressed_image < threshold_min)

weak_i, weak_j = np.where((non_max_supressed_image <= threshold_max) & (non_max_supressed_image >= threshold_min))

threshold_image[strong_i, strong_j] = strong
threshold_image[weak_i, weak_j] = weak

image_after_thresholding = copy.deepcopy(threshold_image)

## Edge Linking
for i in range(1, rows-1):
    for j in range(1, columns-1):
        if (threshold_image[i,j] == weak):
            if ((threshold_image[i+1, j-1] == strong) or (threshold_image[i+1, j] == strong) or (threshold_image[i+1, j+1] == strong)
                    or (threshold_image[i, j-1] == strong) or (threshold_image[i, j+1] == strong)
                    or (threshold_image[i-1, j-1] == strong) or (threshold_image[i-1, j] == strong) or (threshold_image[i-1, j+1] == strong)):
                    threshold_image[i, j] = strong
            else:
                 threshold_image[i, j] = 0

while(True):
    # cv2.imshow("Image after Gaussian Blur",after_agussian_blur)
    # cv2.imshow("sobel_x_image",sobel_x_image)
    # cv2.imshow("sobel_y_image",sobel_y_image)
    # cv2.imshow("sobel_image Image",sobel_image)
    # cv2.imshow("Non maximum supressed Image",non_max_supressed_image)
    cv2.imshow("Image After Thresholding ",image_after_thresholding)
    cv2.imshow("Edge Linked Image",threshold_image)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()