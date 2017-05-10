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
	<style type="text/css">
	</style>
</head>
<body> 
	<?php
	/*********************************************************************
	*
	* 	DBTEST.PHP
	*		Connect to database SRS, Varify if conenction is VALID
	*		Get the QUERY from DBquery.html
	*		Execute the query if query is valid.
	*
	*********************************************************************/
		/*********************************************************************
		*
		* 	Set up local variables for the DB connection
		*
		*********************************************************************/
		$servernamesql 	= "localhost";
		$usernamesql 	= "root";
		$passwordsql 	= "cite30363";
		$dbsql 			= "srs";

		extract($_POST);

		#get the query from the user 
		$query = $_POST["txtarea"]; #$("#query_content").val();

		$queryHTML = htmlspecialchars($query);
		print "query = $queryHTML <br/><br />";

		/*********************************************************************
		*
		* 	Make connection to DB
		*
		*********************************************************************/
		$conn = mysqli_connect($servernamesql,$usernamesql,$passwordsql, $dbsql);

		if(!$conn){
			die("Connection failed: " .mysqli_connect_error());
		}
		echo "Connected to DB server </br>";

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
	?>
</body>
</html>
