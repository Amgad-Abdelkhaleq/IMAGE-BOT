import keras_craft
from helpers import *
import os
import json 

detector = keras_craft.Detector()

def extract_images_tags(filename):
    fname = os.path.join(os.getcwd(),"static/KB/tags.json")                        
    tags_KB = json.load(open(fname,'r')) # load the current data
    folder=os.path.join(os.getcwd(),"static/images/photo")
    global detector 
    image_path = [os.path.join(folder,filename)]
    if os.path.isfile(image_path[0]):
        all_boxes,cropped_images = detector.detect(image_path,return_cropped_images=True)                
        for cropped_boxes in cropped_images: 
            tags=set()
            for cropped_box in cropped_boxes:
                tags.add(extract_text(cropped_box,custom_config = r'-l eng -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6').lower())
                print(tags)
            tags_KB.append({"image":filename , "tags":'++'.join(tags)}) 
        # then we dump it to the file.
        json.dump(tags_KB, open(fname, 'w'))
    else: print("file not found")


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



