<html><head>
<title>PHP test</title></head><body>
<table border="3">
<?php
foreach ($_POST as $key=>$value)
   print("<tr><td>$key</td>".
         "<td>$value</td></tr>");
?>
</table>
</body></html>
