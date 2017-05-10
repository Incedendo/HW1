// <!-- 
//   Kiet Nguyen
//   Lab 2 HTML CSS Javascript
//   CS 30306
//   Professor Payne
// -->

// validatorr.js
//   Register the event handlers for validator.html

$(function() {
      //document.getElementById("first_name").onchange = chkFName;
      
      $("#userEmail").change(function(){
         chkEmail();
      });
      
      // $("#submit").mouseenter(function(){
      // var checkSelect = 0;
        
      //    if($("#dept").val() === "default"){
      //     $("#dept").css("background-color", "Yellow");
      //             alert("You have to choose a DEPARTMENT");
      //             checkSelect = 1;
      //             $("#dept").focus()
      //    }

      // });
});