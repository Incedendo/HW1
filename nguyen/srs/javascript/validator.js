// <!-- 
//   Kiet Nguyen
//   Lab 1 HTML CSS Javascript
//   CS 30306
//   Professor Payne
// -->

// The event handler function for the phone number text box

function chkFName() {

  var pos = $("#first_name").val().search(/^[A-Z]{1}[a-z]{1,}$/);
  if (pos !== 0) {
    alert("The First Name you entered (" + $("#first_name").val() +
      ") is not in the correct form. \n" +
      "The correct form is: John \n" +
      "Please go back and fix your first name");
    $("#first_name").val("");
    $("#first_name").focus();
  } 
}

function chkMName() {

  var pos = $("#middle_name").val().search(/^[A-Z]\.?$/);

  if (pos != 0) {
    alert("The Middle Name you entered (" + $("#middle_name").val() +
      ") is not in the correct form. \n" +
      "The correct form is: J. or J \n" +
      "Please go back and fix your Middle Name");
    $("#middle_name").val("");
    $("#middle_name").focus();
  } 
}

function chkLName() {

  // Test the format of the input phone number

  var pos = $("#last_name").val().search(/^[A-Z]{1}[a-z]{1,}$/);

  if (pos != 0) {
    alert("The Last Name you entered (" + $("#last_name").val() +
      ") is not in the correct form. \n" +
      "The correct form is: Smith \n" +
      "Please go back and fix your Last Name");
    $("#last_name").val("");
    $("#last_name").focus();
  } 
}


function chkEmail() {

  // Test the format of the input phone number

  var pos = $("#Email").val().search(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);

  if (pos != 0) {
    alert("The email you entered (" + $("#Email").val() +
      ") is not in the correct form. \n" +
      "The correct form is: myname@company.com \n" +
      "Please go back and fix your email");
    $("#Email").val("");
    $("#Email").focus();
  } 
}

function chkDept(){
  if($("#dept").val() === "default"){
      alert("You have to choose a DEPARTMENT");
      $("#dept").focus()
  }else{
    $("#dept").css("background-color", "#efffe0");
  }
}

function chkClass(){
  if($("#class").val() === "default"){
      alert("You have to choose a Classification");
      $("#class").focus()
  }else{
    $("#class").css("background-color", "#efffe0");
  }
}

