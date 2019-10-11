import cv2 as cv
import numpy as np
from PIL import Image
from math import pow

def disparity_ssd(L, R, scale):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    # """
    # L = cv.imread('input/pair1-L.png',0)
    # R = cv.imread('input/pair1-R.png',0)

    # TODO: Your code here
    #Define the template
    windows = 4
    # Get the column and row
    row = int(L.shape[0])
    column = int(L.shape[1])
    list = []

    # res = cv.matchTemplate(L,R[20:30, 50:70],method = cv.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # print(min_val, max_val, min_loc, max_loc)
    # exit()
    result = Image.new("L", (row+10, column+10), 0) 
    result_img = result.load()
    #Add padding
    #L = cv.copyMakeBorder(L,0,row,0,row,cv.BORDER_CONSTANT)
    #R = cv.copyMakeBorder(R,0,row,0,row,cv.BORDER_CONSTANT)
    L_pad = np.zeros([windows*2+row, windows*2+column])
    L_pad[windows:row+windows, windows:column+windows] = L
    # print(L.shape)
    #Initialize the SSD image

    #Get the coordinates of the image(Looping through)
    for y in range(windows, row+windows):
        for x in range(windows, column+windows):
    #Supposed to loop through every point in the line
            template = R[y-windows:y+windows,x-windows:x+windows]
            # print(template)
            # exit()
            # print(template.type())
            # print(L.dims())
            # print('------------')
            #disparity += pow(R[int(y+i-windows/2), int(x+j-windows/2)] - L[int(y + i - windows/2),int(d + j - windows/2)], 2)
            res = cv.matchTemplate(L[y-windows:y+windows,:],template,method = cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res) 

            #list.append(max_loc[0]-x)

            result_img[y,x] = abs(max_loc[0]-x)*scale

            print(y/row)

            # exit()
                    #print(j)
            # print(disparity)
    return result
            
            


















   
    
