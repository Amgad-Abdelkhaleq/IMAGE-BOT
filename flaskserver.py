from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__)

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
            print("flask will send this:",userText)
            newdata = {"question": userText} # this is the new data you're going to send to the Node server
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
        print(request.files)
        print("inside post")
        UPLOAD_FOLDER =os.path.join(os.getcwd(),"static/images/text-based")
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
        # Get the name of the uploaded files
        uploaded_files =  request.files.getlist("files")
        print("before for")
        print(uploaded_files)
        #if(len(uploaded_files)==0): raise("files list is empty")
    #     for file in uploaded_files:
    #         if file and allowed_file(file.filename):
    #             print("allowed is okay")
    #             filename = secure_filename(file.filename)
    #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
    #             text=extract_text(image)
    #             data_dict= {"image":filename ,"body":text}
    #             print(data_dict)
    #             fname =  os.path.join(os.getcwd(),"static\KB\output.json")
    #             if os.path.isfile(fname):
    #                 # File exists
    #                 print("file exists")
    #                 with open(fname, 'a+') as outfile:
    #                     outfile.seek(-1, os.SEEK_END)
    #                     outfile.truncate()
    #                     outfile.write(',')
    #                     json.dump(data_dict, outfile)
    #                     outfile.write(']')
    #                     print("kb updated")
    # return render_template("index.html")


if __name__ == "__main__":
   app.run(host='localhost', port=8800)
