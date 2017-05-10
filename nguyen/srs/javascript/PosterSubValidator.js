// <!-- 
//   Kiet Nguyen
//   Lab 1 HTML CSS Javascript
//   CS 30306
//   Professor Payne
// -->

// The event handler function for the phone number text box
function chkEmail() {

  // Test the format of the input phone number

  var pos = $("#userEmail").val().search(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);

  if (pos != 0) {
    alert("The email you entered (" + $("#userEmail").val() +
      ") is not in the correct form. \n" +
      "The correct form is: myname@company.com \n" +
      "Please go back and fix your email");
    $("#userEmail").val("");
    $("#userEmail").focus();
  } 
}

