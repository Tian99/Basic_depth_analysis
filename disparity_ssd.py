import cv2 as cv
import numpy
from PIL import Image
from math import pow

def disparity_ssd(L, R, scale):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    # TODO: Your code here
    #Define the template
    windows = 4
    # Get the column and row
    row = int(L.shape[0])
    column = int(L.shape[1])
    smallest = 100
    disparity = 0
    smallest_list = []
    
    coordinate_list = []
    coordinate = None

    count = 0

    #Add padding
    L = cv.copyMakeBorder(L,0,row,0,row,cv.BORDER_CONSTANT)
    R = cv.copyMakeBorder(R,0,row,0,row,cv.BORDER_CONSTANT)
    # print(L.shape)
    #Initialize the SSD image
    SSD = Image.new("L", (row, column), 0) 
    SSD_img = SSD.load()

    #Get the coordinates of the image(Looping through)
    for y in range(0, row):
        for x in range(0, column):
    #Supposed to loop through every point in the line
            for d in range(0, column): #As it goes on, it only needs to check the line afterward
                disparity = 0 #Reset the disparity
                
                #Calculate the sum in each template
                for i in range(0, windows-1):
                    for j in range(0, windows-1):

                            disparity += pow(R[int(y+i-windows/2), int(x+j-windows/2)] - L[int(y + i - windows/2),int(d + j - windows/2)], 2)
                            
                           # print(j)
                # print(disparity)
                

                if disparity < smallest:
                    smallest = disparity
                    distance = d
                    #print(distance)

            # print('-----------------')
            # print(smallest)
            # print(distance)
            # print(x)
            # print('-----------------')
            # if count ==10:
            #     exit()
            # count+=1


            #smallest_list.append(smallest)
            SSD_img[y, x] = int(abs(distance-x))*scale #Multiply 80 when doing a
            #print(SSD_img[y,x])
            smallest = 100

        print(y/row)

    return SSD
            


















   
    
