from cv2 import cv2 
import pytesseract 

def extract_image_tags(image_name):
    img=cv2.imread(str(image_name)) 
    # Preprocessing the image starts 
    # Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Performing OTSU threshold 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    # Specify structure shape and kernel size.  
    # Kernel size increases or decreases the area  
    # of the rectangle to be detected. 
    # A smaller value like (10, 10) will detect  
    # each word instead of a sentence. 
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
    # Appplying dilation on the threshold image 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
    # Finding contours 
    _,contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                 cv2.CHAIN_APPROX_NONE) 
    # Creating a copy of image 
    im2 = img.copy() 
    # Looping through the identified contours 
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    text=[]
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 
        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
       # Cropping the text block for giving input to OCR 
        cropped = im2[y:y + h, x:x + w] 
        #set languaege as english and set whitelist for chars and digits
        #custom_config = r'-l eng -c tessedit_char_whitelist=" "abcdefghijklmnopqrstuvwxyz --psm 6'
        custom_config = r'-l eng -c tessedit_char_whitelist=" "0123456789abcdefghijklmnopqrstuvwxyz --psm 6'
        # Apply OCR on the cropped image 
        text.append(pytesseract.image_to_string(cropped, config=custom_config).replace("\n"," ")) 
        #code for text preprocessing here (kill tags with two char)
    return text  
    

    
    
    
    
# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = r'E:\4TH\2nd-term\Image Processing\project\tess\tesseract.exe'
      
# Read image from which text needs to be extracted 
img_name= "zero_one.jpg" 
t=extract_image_tags(img_name)
print(t)