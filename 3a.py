from gaussian import noisy
from ps2 import ps2

import os
import cv2

img_1 = cv2.imread(os.path.join('input', 'pair1-L.png'), 0)
img_2 = cv2.imread(os.path.join('input', 'pair1-R.png'), 0)

img_L = noisy(img_1)
img_R = noisy(img_2)

cv2.imwrite('input/pairL_gau.png', img_L)
cv2.imwrite('input/pairR_gau.png', img_R)


ps2('pairL_gau.png', 'pairR_gau.png', 'output/ps2-3-a-1.bmp', 'output/ps2-3-a-2.bmp', 1)
