import keras_craft
from helpers import *
import os
import json 


#exist KB to test find_tag only 
#tags_list= [{'image': '1.jpg', 'tags': {'', 'mohamed', 'co founder/managin', 'varg', 'ss', 'ismail', 'im', 'director', 'salama', 'at', 'tayarah', 'in', 'el-a@'}}, {'image': '2.jpg', 'tags': {'google'}}, {'image': '3.JPG', 'tags': {'the', '', 'things', '(*', 'tof'}}, {'image': '4.jpg', 'tags': {'', 'uta', 'eal'}}, {'image': '5.JPG', 'tags': {'eb.\noo'}}, {'image': '6.jpg', 'tags': {'ond', 'incorta.', 'ee'}}, {'image': 'blur.jpg', 'tags': set()}]

def extract_images_tags(filename):
    fname = os.path.join(os.getcwd(),"static/KB/tags.json")                        
    tags_KB = json.load(open(fname,'r')) # load the current data
    folder=os.path.join(os.getcwd(),"static/images/photo")
    detector = keras_craft.Detector()
    # for filename in os.listdir(folder):
    image_path = [os.path.join(folder,filename)]
    all_boxes,cropped_images = detector.detect(image_path,return_cropped_images=True)
    for cropped_boxes in cropped_images: 
        tags=set()
        for cropped_box in cropped_boxes:
            tags.add(extract_text(cropped_box,custom_config = r'-l eng -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6').lower())
        tags_KB.append({"image":filename , "tags":'++'.join(tags)}) 
    # then we dump it to the file.
    json.dump(tags_KB, open(fname, 'w'))

#extract_images_tags("1.jpg")

def find_tag(entered_tag):
    fname = os.path.join(os.getcwd(),"static/KB/tags.json")                        
    tags_KB = json.load(open(fname,'r')) # load the current data
    entered_tag=entered_tag.lower() #commet this line for testing
    tag_words=entered_tag.split(" ")
    for word in tag_words:
        found=False
        for dic in tags_KB:
            for tag in dic["tags"].split("++"):
                if word==tag: 
                    found=True
                    break 
            if found: return dic 
    return "not found"    


print(">",find_tag("AMR SALAMA"))
