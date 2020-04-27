from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import requests
import json
from helpers import *
from preprocess import *
from tag_extraction import find_tag
import os 

 

app = Flask(__name__)
#create tags KB by calling this func or use exists KB in tag_extension.py
# extract_images_tags()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=['GET'])
def get_bot_response():
        userText = request.args.get('msg')
        if("extract:" in userText):
            image_str=userText[userText.find(":")+1:]
            print(image_str)
            path=os.getcwd()+"/static/images/text-based/"+image_str
            image  = cv2.imread(str(path))
            text = extract_text(image)
            print(text)
            result={"Answer":text,"image_name":image_str,"type":"extract"}
            return result

        elif("tag:" in userText):
            tag=userText[userText.find(":")+1:]
            print("tag entered: ",tag)
            search_result=find_tag(tag)
            if search_result== "not found":
               result={"Answer":"not found","image_name":search_result ,"type":"tag"}
            else:
               result={"Answer": "found" ,"image_name":search_result["image"] ,"type":"tag"}  
            return result  

        elif(userText=="help"):
            help_message="you can ask me any question related to text content in your image and I'll help you find the answer and its image, you also can use extract feature by typing 'extract:' followed by image name to extract text content in the image and 'tag:' followed by a keyword to find any natural image with this tag"
            return {"Answer":help_message ,"type":"help"} 

        
        else:
            print("flask will send this:",userText)
            newdata = {"question": userText} # this is the new data we are going to send to the Node server
            # now immediately sending a post request with new data
            try:
                post = requests.post('http://localhost:3000/postdata', json=newdata) # the POST request      
                print(">>>>>>>>>flask recived this :",post.text)
                result=json.loads(post.text) 
                return result
            except:
                print("i failed connecting node")

      
    

@app.route("/upload",methods=['POST'])
def uploader():
    if request.method == 'POST':
        print(request.files.to_dict())
        print("inside post")
        UPLOAD_FOLDER =os.path.join(os.getcwd(),"static/images")
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
        # Get the name of the uploaded files
        uploaded_files =request.files.getlist("file[]")
        print("before for")
        print(uploaded_files)
        images_names=[]

        for file in uploaded_files:
            if file and allowed_file(file.filename):
                print("allowed is okay")
                filename = secure_filename(file.filename)
                if(len( extract_text(cv2.imread(file)) )<200): 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'],"photo" ,filename))

                else: 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'],"text-based",filename))
                    images_names.append(filename)

        if(len(images_names)): insert_into_KB(images_names)


    return render_template("index.html")


if __name__ == "__main__":
   app.run(host='localhost', port=9877,debug=True)



    
       























 

 
