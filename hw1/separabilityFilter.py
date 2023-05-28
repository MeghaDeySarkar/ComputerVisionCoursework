import cv2
import numpy as np
demo = [[99,96,51,36,9],[15,123,15,99,63],[72,66,3,51,87],[54,60,96,87,102],[75,60,72,93,84]]

demonp = np.float64(np.asarray(demo))
rows = len(demonp)
cols = len(demonp[0])

ker = np.float64([0.33,0.33,0.33])

out_arr = np.zeros([rows,cols])

for i in range(rows):
    for j in range(cols-2):
        out_arr[i][j+1] = (demonp[i][j]*ker[0])+(demonp[i][j+1]*ker[1])+(demonp[i][j+2]*ker[2])

print(">>>")
print(out_arr)

out_arr_final = np.zeros([rows,cols])

for i in range(cols):
    for j in range(rows-2):
        out_arr[j+1][i] = (out_arr[j][i]*ker[0])+(out_arr[j+1][i]*ker[1])+(out_arr[j+2][i]*ker[2])

print("out_arr2")
print(out_arr)
