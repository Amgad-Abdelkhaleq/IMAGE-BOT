var express = require('express');
var bodyParser = require('body-parser');
var bm25_model = require("./BM25"); 
var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

//route to recive user question from flask server 
app.post("/postdata", (req, res) => {
    var question = req.body.question;
    console.log("express recieved:  "+question);
    //call find_ans function to get question answer from the model and then send it back to flask server 
    res.send(bm25_model.find_ans(question));
});

port=7000
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))

