from cv2 import cv2 
import keras_craft
import pytesseract
from helpers import *
import os


#tags_list=[] 

#exist KB to test find_tag only 
tags_list=[{'image': 'amr.jpg', 'tags': {'', 'director', 'mohamed', 'ss', 'co founder/managin', 'in', 'im', 'salama', 'tayarah', 'varg', 'el-a@', 'ismail', 'at'}}, {'image': 'blur.jpg', 'tags': set()}, {'image': 'google.jpg', 'tags': {'gle\nre es ee a'}}, {'image': 'internet.JPG', 'tags': {'', 'things', 'the', 'tof', '(*'}}, {'image': 'menu.jpg', 'tags': {'', 'uta', 'eal'}}]
def extract_images_tags(folder=os.path.join(os.getcwd(),"static/images/photo")):
    global tags_list
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
    global tags_list
    entered_tag=entered_tag.lower() #commet this line for testing
    tag_words=entered_tag.split(" ")
    for word in tag_words:
        found=False
        for dic in tags_list:
            for tag in dic["tags"]:
                if word==tag: 
                    found=True
                    break 
            if found: return dic 
    return "not found"    


# print(">",find_tag("internet of things"))
