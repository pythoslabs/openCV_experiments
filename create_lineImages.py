# Create line images from normal images 
# Inoput dir = ../images 
# Output dir= ../result 

import cv2
import os 
import numpy as np

DIR =  '../images'
OUT_DIR = '../result'

# -------------------- Functions 

def get_lineimage(img) : 

	kernel = np.ones((4,4),np.uint8)	
	#se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (16, 16))
	#bg = cv2.morphologyEx(img, cv2.MORPH_DIALATE, se)
	bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
	result = cv2.divide(img, bg, scale=255)
	
	# Try with custom kernel
	#kernel = np.ones((7,7),np.uint8)
	#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	#result = cv2.divide(img, opening, scale=255)
	return result 

for cur_image in os.listdir(DIR):	
		#img =  cv2.imread(f"{DIR}/{cur_image}", cv2.IMREAD_COLOR)
		img =  cv2.imread(f"{DIR}/{cur_image}", cv2.IMREAD_GRAYSCALE)
		cv2.imwrite(f'{OUT_DIR}/{cur_image}', get_lineimage(img) ) 