import cv2
import os
import numpy as np

path_to_images = './windows'
ideal_larger_size = 800

def resize_image(image):
    height, width = image.shape[:2]
    if width >= height:
        ratio = height/width
        new_height = int(ideal_larger_size*ratio)
        image = cv2.resize(image, (ideal_larger_size, new_height))
    else:
        ratio = width/height
        new_width = int(ideal_larger_size*ratio)
        image = cv2.resize(image, (new_width, ideal_larger_size))
    return image

def save_new_image(image, image_name):
    new_image_name = 'processed_' + image_name
    cv2.imwrite(new_image_name, image)

for image_name in os.listdir(path_to_images):
    if 'jpg' in image_name.lower() or 'jpeg' in image_name.lower():
        image_path = path_to_images + '/' + image_name
        image = cv2.imread(image_path)
        image = resize_image(image)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        # cv2.imshow('edges', image)
        # cv2.waitKey(0)

