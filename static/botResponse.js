function getBotResponse() {
    //get user input 
    var rawText = $("#textInput").val();
    //show it to user in chating  box
    var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    // get request to flask server to get answer for user question
        $.get("/chat", { msg: rawText }).done(function(data) {
          // check the type of response wether it will be only text or image or both  
          if(data.type=="extract" || data.type=="help" || data.type=="error"){
              //case text only response
              var botHtml = '<p class="botText">' + data.Answer + '</p>';
              $("#chatbox").append(botHtml);
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'}); 
          }
          
          else if(data.type=="tag"){
              if(data.Answer == "not found"){
              //if answer does not exists will return "not found" to user 
              var botHtml = '<p class="botText">' + data.Answer + '</p>';
              $("#chatbox").append(botHtml);
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'}); 
          }
          
          else if(data.Answer == 'found'){
              //if answer is found return text answer and its image 
              rand ='_' + Math.random().toString(36).substr(2, 9);
              var imagehtml= 
              '<div class="thumb" href="#">'
                +'<img src="" alt="" id="imageBox">'
                +'<div class="caption">'+"&nbsp;"+data.image_name +'</div>'
                +'</div>'              
              $("#chatbox").append(imagehtml);
              document.getElementById('imageBox').id=rand
              document.getElementById(rand).src = "../static/images/photo/"+data.image_name; 
              document.getElementById(rand).alt= data.image_name;
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
              } 
          }


          else {
              var botHtml = '<p class="botText">' + data.Answer + '</p>';
              $("#chatbox").append(botHtml);
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
              if(data.Answer != 'not found'){
              rand ='_' + Math.random().toString(36).substr(2, 9);
              var imagehtml= 
            '<div class="thumb" href="#">'
                +'<img src="" alt="" id="imageBox">'
                +'<div class="caption">'+"&nbsp;"+data.image_name +'</div>'
                +'</div>'             
              $("#chatbox").append(imagehtml);
              document.getElementById('imageBox').id=rand
              document.getElementById(rand).src = "../static/images/text-based/"+data.image_name; 
              document.getElementById(rand).alt= data.image_name;
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
                        }
          } 
        });
     }
 

  $("#textInput").keypress(function(e) {
      if(e.which == 13) {
          getBotResponse();
      }
  });
  $("#buttonInput").click(function() {
    getBotResponse();
  })