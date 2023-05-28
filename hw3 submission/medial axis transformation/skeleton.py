import cv2
import numpy as np
import copy

# Load the image and convert to grayscale
image = cv2.imread('cvSmall.png',cv2.IMREAD_GRAYSCALE)

# Threshold the image to obtain a binary image
ret, binary_image = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)

# Invert the binary image to make object pixels 1 and background pixels 0
binary_image = cv2.bitwise_not(binary_image)

# Create a copy of the thresholded image for visualization purposes
threshold_backup = copy.deepcopy(binary_image)

# Initialize the skeleton image as an all-zero array of the same size as the thresholded image
skeleton = np.zeros_like(binary_image)

# Perform the medial axis transform using a for loop
while np.sum(binary_image) > 0:
    # Erode the thresholded image
    eroded = cv2.erode(binary_image, None)
    # Dilate the eroded image to obtain a temporary image
    temp = cv2.dilate(eroded, None)
    # Subtract the temporary image from the original thresholded image
    temp = cv2.subtract(binary_image, temp)
    # Use a bitwise OR operation to add the temporary image to the skeleton image
    skeleton = cv2.bitwise_or(skeleton, temp)
    # Update the thresholded image to be the eroded image
    binary_image = eroded.copy()

# Display the original image, the thresholded image, and the resulting skeleton image
while(True):
    cv2.imshow('original image', image)
    cv2.imshow("Binary image (inverted pixels)",threshold_backup)
    cv2.imshow("Skeleton image",skeleton)

    # Wait for the user to press the 'ESC' key to exit
    if cv2.waitKey(1) == 27:
        break

# Destroy all open windows
cv2.destroyAllWindows()