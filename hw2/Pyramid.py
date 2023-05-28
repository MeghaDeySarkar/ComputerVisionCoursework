import numpy as np
import cv2

pic = cv2.imread('Lenna.png')
grayscale = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

no_of_levels = 5
error_image = []

def gaussian_pyramid(image, no_of_levels):
    img_pyramid = [image]
    for i in range(no_of_levels-1):
        image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
        img_pyramid.append(image)
        
    return img_pyramid

# Calling Gaussian pyramid function with level 5
pyramid = gaussian_pyramid(grayscale, 5)
cv2.imshow('Downsampled to 32 x 32 ', pyramid[no_of_levels-1]) # Displaying the last downsampled image (32x32)

# Displaying error image
for i in range(len(pyramid)):
    if i > 0:
        error = cv2.subtract(pyramid[i-1], cv2.resize(pyramid[i], (pyramid[i-1].shape[1], pyramid[i-1].shape[0])))
        cv2.imshow('Error ' + str(i-1), error)
        error_image.append(error)


# Reconstructing the original image using 32 X 32 image and error images

reconstructed_img = pyramid[no_of_levels-1] # Storing 32 X 32 for reconstruction
for j in range(3,-1,-1):
    
    reconstructed_img = cv2.resize(reconstructed_img, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # Reconstructing the original image by upsampling
    
    reconstructed_img = cv2.add(reconstructed_img, error_image[j]) # Adding the error image 
    cv2.imshow('reconstructed_img ' + str(j), reconstructed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()