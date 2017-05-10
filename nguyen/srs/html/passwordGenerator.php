<!-- 
  Kiet Nguyen
  Lab 2 SRS 
  CS 30306
  Professor Payne
-->
<html>
<head>
	<title>
		Testing DB Access
	</title>
	<style type="text/css"></style>
</head>

<body>
	<?php
	/*********************************************************************
	*
	* 	Upon submission of new abstract and title, generate a unique Poster ID
	*	and 8-char passwords for users
	*
	*********************************************************************/
		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			echo "Welcome " .$_POST["first_name"]. "<br>";
			echo "Your email address is: " .$_POST["email"]."<br>"; 
			$posterID 		= uniqid();
			echo "Your UNIQUE Poster ID  is: " .$posterID ."<br>"; 
			echo "Your dept is: " .$_POST["deptOption"]."<br>"; 
			echo "Your classification is: " .$_POST["classOption"]."<br>"; 
			
			/*********************************************************************
			*
			* 	Generate a random 8-character password for user
			*
			*********************************************************************/
			function randomPassword() {
			   $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
			   $pass = array(); //remember to declare $pass as an array
			   $alphaLength = strlen($alphabet) - 1; //put the length -1 in cache
			   for ($i = 0; $i < 8; $i++) {
			       $n = rand(0, $alphaLength);
			       $pass[] = $alphabet[$n];
			   }
			   return implode($pass); //turn the array into a string
			}

			$pwd = randomPassword();
			echo "Your 8 character password is " .$pwd. "<br>";

			/*********************************************************************
			*
			* 	Set up local variables for the DB connection
			*
			*********************************************************************/
			$servername = "localhost";
			$username 	= "root";
			$password 	= "cite30363";
			$db 		= "srs";
			/*********************************************************************
			*
			* 	Set up local variables for the query
			*
			*********************************************************************/
			$fname 			= $_POST["first_name"];
			$MI 			= $_POST["middle_name"];
			$lname 			= $_POST["last_name"];
			$email 			= $_POST["email"];
			$projTitle 		= $_POST["projTitle"];
			$abstract 		= $_POST["abstract"];
			$dept 			= $_POST["deptOption"];
			$classification = $_POST["classOption"];
			$PSWD 			= $pwd;
			
			extract($_POST);

			$query = "
				INSERT INTO SRSsubmissions 
				VALUES " ."('$posterID', '$dept', '$classification', '$lname', 
				'$fname', '$MI', '$email', '$PSWD', '$projTitle', '$abstract')
			";

			$queryHTML = htmlspecialchars($query);
			#print "query = $queryHTML <br/><br />";

			/*********************************************************************
			*
			* 	Make connection to DB
			*
			*********************************************************************/
			$conn = mysqli_connect($servername,$username,$password, $db);

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

			if(preg_match("/^select/i",$query, $match)){
				echo "***** Dumping result of $match[0]***** <br />";
				while($row = mysqli_fetch_assoc($result)){
					foreach($row as $k => $v){
						print "$k, $v ";
					}
					print "<br />";
				}
				mysqli_free_result($result);
			}

			mysqli_close($conn);
		}
	?>
</body>
</html>
