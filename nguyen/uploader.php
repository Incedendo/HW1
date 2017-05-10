<html>
<head><title>PHP File Upload </title></head>
<body>

<?php
// Accept file and move to a different location or is deleted.
// Access through $_FILES global array
// $_FILES['uploadedfile']['name'] - name is original path of user's file
// $_FILES['uploadedfile']['tmp_name'] - path to the temp file on server


// Where the file is going to be placed 
$target_path = "uploads/";

/* Add the original filename to our target path.  
Result is "uploads/filename.extension" */

$target_path = $target_path . basename( $_FILES['uploadedfile']['name']); 

print "\$target_path = $target_path <br /> ";

if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file ".  basename( $_FILES['uploadedfile']['name']). 
    " has been uploaded";
} else{
    echo "There was an error uploading the file. Err code = " .  $_FILES[‘uploadedfile’][‘error’] ;

}
echo "<br /><br />*** Display of values from \$_FILES['uploadedfile'][...] global array ****";
foreach ($_FILES['uploadedfile'] as $key=>$value)
   		print("<br />$key = $value");



?>


</body></html>