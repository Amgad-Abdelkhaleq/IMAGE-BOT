var express = require('express');
var bodyParser = require('body-parser');
var bm25_model = require("./BM25"); 
var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.post("/postdata", (req, res) => {
    var question = req.body.question;
    //var  KB = req.body.KB;
    console.log("express recieved:  "+question);
    res.send(bm25_model.find_ans(question));
});

port=4000
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))

