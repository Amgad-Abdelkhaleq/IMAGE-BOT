from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import requests
import json

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
    newdata = {"question": userText} # this is the new data you're going to send to the Node server
    # now immediately sending a post request with new data
    post = requests.post('http://localhost:5000/postdata', json=newdata) # the POST request
    print(">>>>>>>>>flask recived this :",post.text)
    # get = requests.get('http://localhost:5000/getdata') # GET request
    # data = get.json()
    # # process this JSON data and do something with it
    # print(">>>>>>>>>>>>>flask recieved this:",data) 
    result=json.loads(post.text)
    return result["Answer"].replace("\n"," ")


if __name__ == "__main__":
   app.run(host='localhost', port=8800)



 

 
