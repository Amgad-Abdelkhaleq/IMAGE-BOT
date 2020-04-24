from cv2 import cv2 
import keras_craft
import pytesseract
from helpers import *
import os

def extract_image_tags(image_name):
    pass

detector = keras_craft.Detector()
image_path = [os.path.join(os.getcwd(),"static/images/photo/amr.jpg")]
all_boxes,cropped_images = detector.detect(image_path,return_cropped_images=True)

for cropped_boxes in cropped_images: 
  print(cropped_boxes,"\n",'.............................')
  for cropped_box in cropped_boxes:
     #gray = get_grayscale(cropped_box)
     #thresh = thresholding(gray)    
     plt.imshow(cropped_box)
     plt.figure()
     print('>',extract_text(cropped_box))

# # Visualization
# for image_path, boxes in zip(image_paths,all_boxes):
#   image_with_boxes_path = keras_craft.draw_boxes_on_image(image_path, boxes)
#   print(image_with_boxes_path)