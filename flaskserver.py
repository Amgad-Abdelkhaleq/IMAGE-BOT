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

@app.route("/get",methods=['POST','GET'])
def get_bot_response():
    if request.method == "POST":
        if(userText=="upload"):
            UPLOAD_FOLDER =os.path.join(os.getcwd(),"static/images/text-based")
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
            # Get the name of the uploaded files
            uploaded_files = request.files.getlist("file[]")
            for file in uploaded_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
                text=extract_text(image)
                data_dict= {"image":filename ,"body":text}
                fname =  os.path.join(os.getcwd(),"static\KB\output.json")
                if os.path.isfile(fname):
                # File exists
                with open(fname, 'a+') as outfile:
                    outfile.seek(-1, os.SEEK_END)
                    outfile.truncate()
                    outfile.write(',')
                    json.dump(data_dict, outfile)
                    outfile.write(']')

    elif request.method == "GET":
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
   app.run(host='localhost', port=9960)



 

 
