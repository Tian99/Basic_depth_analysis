# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def enhance():
	image = cv2.imread('input/pair1-L.png', cv2.IMREAD_GRAYSCALE)
	image_enhanced = cv2.equalizeHist(image, 100)

	cv2.imwrite('input/enhanced_L.png', image_enhanced)