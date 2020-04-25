from cv2 import cv2 
import keras_craft
import pytesseract
from helpers import *
import os

def extract_images_tags(folder=os.path.join(os.getcwd(),"static/images/photo")):
    tags_list=[]
    detector = keras_craft.Detector()
    for filename in os.listdir(folder):
        image_path = [os.path.join(folder,filename)]
        all_boxes,cropped_images = detector.detect(image_path,return_cropped_images=True)
        for cropped_boxes in cropped_images: 
            tags=set()
            for cropped_box in cropped_boxes:
                # plt.imshow(cropped_box)
                # plt.figure()
                tags.add(extract_text(cropped_box,custom_config = r'-l eng -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6').lower())
            tags_list.append({"image":filename , "tags":tags}) 
        # # Visualization
        # for image_path, boxes in zip(image_paths,all_boxes):
        #   image_with_boxes_path = keras_craft.draw_boxes_on_image(image_path, boxes)
        #   print(image_with_boxes_path)
    return tags_list

# print(extract_images_tags())

def find_tag(entered_tag):
    entered_tag=entered_tag.lower()
    found=False
    tag_list=extract_images_tags()
    for dic in tag_list:
        for tag in dic["tags"]:
            if entered_tag==tag: 
                found=True
                break 
        if found: return dic 
    return "not found"    

print(find_tag('amr'))