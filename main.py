import cv2
import os

path_to_images = './windows'

def resize_image(image):
    height, width = image.shape[:2]
    print(width/height)
#     if width >= height:
#         if width != 500 or height != 340:
#             print 'not right size'
#             image = cv2.resize(image, (500, 340))
#             cv2.imwrite(image_path, image)
#     else:
#         if height != 500 or width != 340:
#             print 'not right size'
#             image = cv2.resize(image, (340, 500))
#             cv2.imwrite(image_path, image)

def search_for_frame(image):
    

for image_name in os.listdir(path_to_images):
    if not 'DS_Store' in image_name:
        image_path = path_to_images + '/' + image_name
        print(image_name)
        image = cv2.imread(image_path)
        #resize_image(image)