function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
        $.get("/chat", { msg: rawText }).done(function(data) {
          if(data.type=="extract" || data.type=="help" || data.type=="error"){
              var botHtml = '<p class="botText">' + data.Answer + '</p>';
              $("#chatbox").append(botHtml);
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'}); 
          }
          
          else if(data.type=="tag"){
              if(data.Answer == "not found"){
              var botHtml = '<p class="botText">' + data.Answer + '</p>';
              $("#chatbox").append(botHtml);
              document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'}); 
          }
          
          else if(data.Answer == 'found'){
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