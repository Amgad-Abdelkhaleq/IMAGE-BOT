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

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),"static/images")
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
<<<<<<< HEAD
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']  
=======
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
>>>>>>> 48a400cf7832a2c92820cc1183a474d86270c106

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=['GET'])
def get_bot_response():
        userText = request.args.get('msg')
        if("extract:" in userText):
            try:    
                image_str=userText[userText.find(":")+1:]
                print(image_str)
                path=os.getcwd()+"/static/images/text-based/"+image_str
                image  = cv2.imread(str(path))
                text = extract_text(image)
                print(text)
                return {"Answer":text,"image_name":image_str,"type":"extract"}
            except:
                return {"Answer":"image not found","type":"error"}    

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
        uploaded_files =request.files.getlist("file[]")
        for file in uploaded_files:
            if file and allowed_file(file.filename):
            print("allowed is okay")
            filename = file.filename
            img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            text= extract_text(img,custom_config = r'-l eng -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --oem 1')
            page= extract_text(img)
            print(len(text),"p:",len(page))
            if(len(text)<200): 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],"photo" ,filename))
            else: 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],"text-based",filename))
                insert_into_KB(page=page,filename=file.filename)         

    return render_template("index.html")


if __name__ == "__main__":
   app.run(host='localhost', port=5000,debug=True)



    
       























 

 
