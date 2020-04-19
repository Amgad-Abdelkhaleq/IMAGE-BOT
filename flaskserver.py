from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import requests
import json
from text_extraction import *
import os 
 

app = Flask(__name__)

#KB_json=json.dumps(KB)
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
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
        #result=json.dumps(result)
        return result

    # elif("tag:" in userText):
    #     #do tag
    #     pass
    #result={"Answer":text,"image_name":image_str,"type":"tag"}
    else:
       newdata = {"question": userText} # this is the new data you're going to send to the Node server
       # now immediately sending a post request with new data
       try:
         post = requests.post('http://localhost:3000/postdata', json=newdata) # the POST request      
         print(">>>>>>>>>flask recived this :",post.text)
         result=json.loads(post.text) 
         return result
       except:
           print("i failed connecting node")
      
       


if __name__ == "__main__":
   app.run(host='localhost', port=9860)



 

 
