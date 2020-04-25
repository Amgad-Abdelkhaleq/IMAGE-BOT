function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
  //  if(rawText=="upload"){
        //  $('#uploadInput').focus().trigger('click');
                        
          //               var uploadForm = document.createElement('form');
          //               var fileInput = uploadForm.appendChild(document.createElement('input'));
          //               fileInput.type = 'file';
          //               fileInput.name = 'file[]';
          //               fileInput.multiple = true;
          //               fileInput.id="uploadInput"
          //               fileInput.click();
          //               //$("#uploadInput").remove();
                    

          // var formdata = new FormData(); //FormData object
          // var fileInput = document.getElementById('#uploadInput');
          // //Iterating through each files selected in fileInput
          // for (i = 0; i < fileInput.files.length; i++) {
          //     //Appending each file to FormData object
          //     formdata.append(fileInput.files[i].name, fileInput.files[i]);
          // }
          // //Creating an XMLHttpRequest and sending
          // var xhr = new XMLHttpRequest();

          // var url = encodeURI('http://localhost:8772/chat');
          // xhr.open('POST', url,true);
          // xhr.send(formdata); 
          
          // xhr.onreadystatechange = function () {
          //     if (xhr.readyState == 4 && xhr.status == 200) {
          //         alert(xhr.responseText);
          //     }
          // }
          // $("#uploadInput").remove();

    // } else{
        $.get("/chat", { msg: rawText }).done(function(data) {
          if(data.type=="extract"){
          var botHtml = '<p class="botText">' + data.Answer + '</p>';
          $("#chatbox").append(botHtml);
          document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'}); 
          }
          
          else if(data.type=="help"){
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
          // var imagehtml='<p class="botimage"><span>'
          //    + '<img src="" width="500" height="500" id="imageBox">' 
          //    +'<p class="image-title">'+data.image_name+'</p>'
          //    + '</span></p>'
          var imagehtml= 
         '<div class="thumb" href="#">'
            +'<img src="" alt="" id="imageBox">'
            +'<div class="caption">'+"&nbsp;"+data.image_name +'</div>'
            +'</div>'
          // '<figure class="botimage">'
          //   +'<img src="" width="500" height="500" id="imageBox">'
          //   +'<figcaption class="image-title">'+data.image_name+'</figcaption>'
          //   +'</figure>'              
          $("#chatbox").append(imagehtml);
          document.getElementById('imageBox').id=rand
          document.getElementById(rand).src = "../static/images/text-based/"+data.image_name; 
          document.getElementById(rand).alt= data.image_name;
          document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});


                    }

          } 

        });
     }
  //}

  // function uploadImage(){
  // // var form_data = new FormData(); //FormData object
  //   var fileInput = document.getElementById('#File');
  //   // if(fileInput.files.length != 0){alert("shit happend")}
  //   //Iterating through each files selected in fileInput
  //   // for (i = 0; i < fileInput.files.length; i++) {
  //   //     //Appending each file to FormData object
  //   //   form_data.append(fileInput.files[i].name, fileInput.files[i]);
  
  //   // }
  //   //var form_data = new FormData($('#File')[0]);
  //     //console.log(form_data)
  //     var formDataRaw = $('#FileForm')[0];
  //     var form_data = new FormData(formDataRaw);
  //     $.ajax({
  //         type: 'POST',
  //         url: '/upload',
  //         data: form_data,
  //         contentType: false,
  //         cache: false,
  //         processData: false,
  //         async: false,
  //         success: function (data) {
  //             console.log('Success!');
  //             $("#status").show();
  //         },
  //     });


  // }


  $("#textInput").keypress(function(e) {
      if(e.which == 13) {
          getBotResponse();
      }
  });
  $("#buttonInput").click(function() {
    getBotResponse();
  })