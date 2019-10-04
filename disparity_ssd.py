import cv2 as cv
import numpy as np

def disparity_ssd(L, R):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    # TODO: Your code here
    # Get the width and height

    height = L.shape[0]
    width = L.shape[1]

    #Initialize the SSD image
    SSD = np.zeros((height, width, 1), np.unit8)

    for y in range(0, height):
        for x in range(0, width):
	
            SSD(y,x) = R(y,x - L(y,x))

    return SSD


    
   
    
