var express = require('express');
var bodyParser = require('body-parser');
var bm25_model = require("./BM25"); ///////////////////////
 
var app = express();


// ans="this is the answer"
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
 
app.post("/postdata", (req, res) => {
    var question = req.body.question;
    //var  KB = req.body.KB;
    console.log("express recieved:  "+question);
    res.send(bm25_model.find_ans(question));
});


// app.get("/getdata", (req, res) => {
//     var data = { // this is the data you're sending back during the GET request
//         data1: answer,
//     }
//     res.status(200).json(data)
// });



port=3000
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))

