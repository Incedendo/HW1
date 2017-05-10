<!-- 
  Kiet Nguyen
  Lab 2 SRS 
  CS 30306
  Professor Payne
-->
<html>
<head><title>PHP File Upload</title></head>
<body>

<?php
// In PHP versions earlier than 4.1.0, $HTTP_POST_FILES should be used instead
// of $_FILES.
/*********************************************************************
*
* 	posterSubValidator.php
*		Get user info and check in DB if that user has signed up 
*		Only let the user upload a PDF if he has previously create a profil
*
*
*
*********************************************************************/

	/*********************************************************************
	*
	* 	Make sure to only proceed if method is POST.
	*
	*********************************************************************/
	if ($_SERVER["REQUEST_METHOD"] == "POST") {

		//Error handling
		error_reporting(-1);
		ini_set('display_errors', 'On');
		set_error_handler("var_dump");

		//DATABSE VERIFICATION
		/*********************************************************************
		*
		* 	Set up local variables for the DB connection
		*
		*********************************************************************/
		$servernamesql 	= "localhost";
		$usernamesql 	= "root";
		$passwordsql 	= "cite30363";
		$dbsql 			= "srs";
		
		//$test = $_POST['userEmail'];
		$email_user 	= $_POST["userEmail"];
		//echo "user email (test) = $test";
		$PSWD 			= $_POST["password"];
		$posterID 		= $_POST["posterID"];

		extract($_POST);
		/*********************************************************************
		*
		* 	get the query to find the DEPT of that user
		*
		*********************************************************************/
		$query = "
			SELECT Dept 
			FROM SRSSubmissions
			WHERE  
			Poster_ID = '$posterID' AND PSWD = '$PSWD' AND PC_Email ='$email_user';
		";

		$queryHTML = htmlspecialchars($query);
		#print "<br />query = $queryHTML <br/><br />";

		/*********************************************************************
		*
		* 	Make connection to DB
		*
		*********************************************************************/
		$conn = mysqli_connect($servernamesql,$usernamesql,$passwordsql, $dbsql);

		if(!$conn){
			die("Connection failed: " .mysqli_connect_error());
		}
		#echo "Connected to DB server </br>";

		/*********************************************************************
		*
		* 	CHECK if connection is valid and PRINT out result
		*
		*********************************************************************/
		if( $result = mysqli_query($conn,$query) ){
			echo "Executed SQL statment <br /><br />";
		}else{
			die("Error executing SQL statement: " .mysql_error($conn) );
		}

		$department = "";
		while($row = mysqli_fetch_assoc($result)){
			foreach($row as $k => $v){				
				$department = $v;
			}
		}
		mysqli_free_result($result);
		
		print "User's Department is: $department <br />";
		mysqli_close($conn);


	/*********************************************************************
	*
	* 	UPLOAD PDF FILE, check if DB can find the DEPT of that user
	*
	*********************************************************************/

		if($department !== ""){
			$uploaddir = $_SERVER['DOCUMENT_ROOT'] ."/nguyen/uploads/" ;
			$uploaddir = $uploaddir ."/". $department."/";
			#echo "\$uploaddir = $uploaddir <br />";
			/*********************************************************************
			*
			* 	CHECK if the DIRECTORY is VALID and can be uploaded to
			*
			*********************************************************************/
			if (is_dir($uploaddir) && is_writable($uploaddir)) {
			   	// do upload logic here
			   	$uploadfile = $uploaddir . basename($_FILES['myFile']['name']);
				#echo "\$uploadfile = $uploadfile <br />";

				/*********************************************************************
				*
				* 	Upload the file and move it to its corresponding DEPT
				*
				*********************************************************************/
				if (move_uploaded_file($_FILES['myFile']['tmp_name'], $uploadfile)) {
				   echo "<br />FILE IS VALID AND WAS SUCCESSFULLY UPLOADED TO $uploaddir.<br />";
				} else {
				   echo "There was an error uploading the file! Error code = " .$_FILES['myFile']['error'] ."<br />";
				}

				// echo 'Here is some more debugging info:';
				// print_r($_FILES);

				// echo "<br /><br />*** Display of value from \$_FILES['myFile'][...] global array ***";
				// foreach ($_FILES['myFile'] as $key => $value) {
				// 	print("<br />$key = $value");
				// }
			}else{
			   echo 'Upload directory is not writable, or does not exist. <br />';
			}
		}else{
			echo "There is no such user. Please enter correct infomation! <br/>";
		}
		

	}
?>
</body></html>
