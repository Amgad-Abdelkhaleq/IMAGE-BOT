import keras_craft
from helpers import *
import os


#tags_list=[] 

#exist KB to test find_tag only 
tags_list= [{'image': '1.jpg', 'tags': {'', 'mohamed', 'co founder/managin', 'varg', 'ss', 'ismail', 'im', 'director', 'salama', 'at', 'tayarah', 'in', 'el-a@'}}, {'image': '2.jpg', 'tags': {'google'}}, {'image': '3.JPG', 'tags': {'the', '', 'things', '(*', 'tof'}}, {'image': '4.jpg', 'tags': {'', 'uta', 'eal'}}, {'image': '5.JPG', 'tags': {'eb.\noo'}}, {'image': '6.jpg', 'tags': {'ond', 'incorta.', 'ee'}}, {'image': 'blur.jpg', 'tags': set()}]

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
