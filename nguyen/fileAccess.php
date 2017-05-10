<html><head>
<title>PHP file access test</title>
<style type="text/css">
	h1, form {text-align:center}
</style>
</head>
<body>	
<h1>File Access Demo</h1>

<?php
$file=$_SERVER['DOCUMENT_ROOT']."/nguyen/uploads/".$_GET['filename'];
if (!file_exists($file)) {
	print "File $file does not exist.";
	print "</body></html>";
	die;

} else
	print "Filename entered:  $file <br />";
?>

File contents: <br />
<?php
$fptr = fopen($file,'r');
if (! $fptr) {
	print "File could not be opened";
} else {

	while (! feof($fptr)) {
	   $line = fgets($fptr,80);	   
	   print "!$line! <br />";
	}
	fclose($fptr);
}			
?>
   
</body></html>
