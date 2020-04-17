var express = require('express');
var bodyParser = require('body-parser');
 
var app = express();
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
 
app.post("/postdata", (req, res) => {
    var question = req.body.question;
    var KB = req.body.KB;
    console.log("express recieved: "+question+ "and >>>>"+KB);
    res.send("process complete");
});
 
app.get("/getdata", (req, res) => {
    var data = { // this is the data you're sending back during the GET request
        data1: "this is the answer",
    }
    res.status(200).json(data)
});
port=5000
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))