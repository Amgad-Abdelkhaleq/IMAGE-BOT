from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import requests

app = Flask(__name__)
kB= [
    {

    "body": "In order to supply electricity into a mains electricity system, the de output from\nthe module smst te converted to ac at the correct voltage and frequency. “n\nelectronic inverter is used to do this. Generally a number of PV modules ar\nconnected in series to provide a higher de voltage to the inverter input, and\nsometimes several of these ‘series strings’ are connected in parallel, so that a single\ninverter can be used for 50 or more modules. Modern inverters are very efficient\n(typically 97%), and use electronic control systems to ensure that the PV array keeps\nworking at its optimum voltage. They also incorporate safety systems as required in\nthe country of use."

    } ,
    {   
 "body": "Many grid connected PV systems are installed on frames which are mounted\non the roof or walls of a building. Used in this way the PV does not take up land that\ncould be used for other purposes. Ideally the PV faces towards the equator (i.e. South\nin the northern hemisphere) but the exact direction is not critical. However, it is\nimportant to make sure that there is minimal shading of the PV. The inverter is\nhoused inside the building and connected to the mains electrical supply, usually with\na meter to measure the kWh generated. If the PV electricity production exceeds\nbuilding demand then the excess can be exported to the grid, and vice versa."
    }, 
    {   
    "body": "Grid Tied Net Metered systems involve connecting your system to the power\ngrid but you use the power, and it offsets your electric bill. If you don’t produce as\nmuch electricity as you use then the grid just supplies the difference and you get\nbilled for that difference, if you produce more than you use, the excess just goes 10\nthe grid. Whether you get paid for that difference that you supply to the grid depentis\n\n"
} 
  ]
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    newdata = {"question": userText, "KB":kB} # this is the new data you're going to send to the Node server
    # now immediately sending a post request with new data
    post = requests.post('http://localhost:5000/postdata', json=newdata) # the POST request
    print(">>>>>>>>>flask sent this :",post.text)
    get = requests.get('http://localhost:5000/getdata') # GET request
    data = get.json()
    # process this JSON data and do something with it
    print(">>>>>>>>>>>>>flask recieved this:",data) 
    return 'fuck u >>>'+userText


if __name__ == "__main__":
   app.run(host='localhost', port=8800)



 

 
