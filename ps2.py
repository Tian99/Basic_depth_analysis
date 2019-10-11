# ps2
import os
import numpy as np
import cv2
from editing import rotate


def ps2(input_L, input_R, output_L, output_R, scale):
	## 1-a
	# Read images
	L = cv2.imread(os.path.join('input', input_L), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
	R = cv2.imread(os.path.join('input', input_R), 0) * (1.0 / 255.0)


	cv2.imwrite("output/1.png", L)
	# Compute disparity (using method disparity_ssd defined in disparity_ssd.py)
	from disparity_ssd import disparity_ssd
	D_L = disparity_ssd(L, R, scale)
	D_L.save(output_L)

	D_R = disparity_ssd(R, L, scale)

	# TODO: Save output images (D_L as output/ps2-1-a-1.png and D_R as output/ps2-1-a-2.png)
	D_R.save(output_R)

	# Note: They may need to be scaled/shifted before saving to show results properly
	rotate(output_L, -90, output_L)
	rotate(output_R, -90, output_R)


	# TODO: Rest of your code here
