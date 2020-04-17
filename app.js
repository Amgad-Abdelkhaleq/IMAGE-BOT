var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");
var app = express();
var http = require("http").Server(app);
var io = require("socket.io")(http);
// var MarkdownIt = require("markdown-it");
var showdown = require("showdown");
var bm25_model = require("./public/javascripts/BM25"); ///////////////////////
// view engine setup
app.engine("html", require("ejs").renderFile);
app.set("view engine", "html");
app.set("views", path.join(__dirname, "views"));
app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

var converter = new showdown.Converter();

//set a socket for communication
io.on("connection", function(socket) {
    console.log("a user connected");
    socket.on("chat message", function(msg) {
        msg = bm25_model.find_ans(msg);
        io.emit("chat message", converter.makeHtml(msg));
    });
    socket.on("disconnect", function() {
        console.log("user disconnected");
    });
});

//routes setup
app.use("/", indexRouter);
app.use("/users", usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get("env") === "development" ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render("error");
});

http.listen(3000, function() {
    console.log("listening on *:3000");
});
module.exports = app;
