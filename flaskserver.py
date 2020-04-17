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
    return 'fuck u >>>'+userText


if __name__ == "__main__":
   app.run(host='localhost', port=8800)
