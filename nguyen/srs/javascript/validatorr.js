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
      $("#first_name").change(function(){
         chkFName();
      });
      $("#middle_name").change(function(){
         chkMName();
      });
      $("#last_name").change(function(){
         chkLName();
      });
      $("#Email").change(function(){
         chkEmail();
      });
      $("#dept").change(function(){
         chkDept();
      });
      $("#class").change(function(){
         chkClass();
      });
      $("#submit").mouseenter(function(){
      var checkSelect = 0;
        
         if($("#dept").val() === "default"){
          $("#dept").css("background-color", "Yellow");
                  alert("You have to choose a DEPARTMENT");
                  checkSelect = 1;
                  $("#dept").focus()
         }

         if($("#class").val() === "default"){
          $("#class").css("background-color", "Yellow");
             alert("You have to choose a Classification");
             checkSelect = 1;
             $("#class").focus()
         }

      });
});

