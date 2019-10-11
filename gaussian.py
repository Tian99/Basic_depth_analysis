import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

def noisy(img):

    sigma = 500 ** 0.6
    row = img.shape[0]
    height = img.shape[1]

    gaussian = np.random.normal(0, sigma, (row, height))

    noisy_image = np.zeros(img.shape, np.float32)

    noisy_image = img + gaussian
    
    noisy_image = noisy_image.astype(np.uint8)

    return noisy_image


# noisy(cv2.imread('input/pair1-L.png', 0))