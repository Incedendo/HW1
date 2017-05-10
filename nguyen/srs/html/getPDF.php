<!-- 
  Kiet Nguyen
  Lab 2 SRS 
  CS 30306
  Professor Payne
-->
<html>
<head><title>PHP PDF Display</title></head>
<body>

<?php
	/*********************************************************************
	*
	* 	PRINT OUT ALL THE PDF FILE of a particular DEPARTMENT.
	*
	*********************************************************************/
	
	/*********************************************************************
	*
	* 	Get the path to the Directory of the specified DEPT
	*
	*********************************************************************/
	$dir = $_SERVER['DOCUMENT_ROOT'] ."/nguyen/uploads";
	$dept = $_GET['dept'];
	$dir = $dir . "/$dept";
	
	echo "Current Directory: $dir <br />";
	echo "<br />List of PDF file in department $dept: <br />";
	
	// Open a directory, and read its contents
	if (is_dir($dir)){
		if ($dh = opendir($dir)){
			$count = 0;
			while ( (($file = readdir($dh)) !== false)  ){
				//exclude the . and .. files
			  	if( strlen($file) >= 4){
			  		$temp_dir = $dir ."/". $file; 
			  		echo "Full Path: " . $temp_dir . "<br>";
			  		echo "<a href='$temp_dir' download='newfilename'>$file</a> <br />";
			  		$count++;
			  	}
			}
			//If the directory has no PDF submission
			if($count == 0){
				echo "*****There is no ENTRY in this DEPARTMENT*****";
			}
			closedir($dh);
		}
	}
?>

</body></html>