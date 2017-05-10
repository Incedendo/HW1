
<html><head>
<title>PHP test</title></head><body>
<table>
<?php
foreach ($_SERVER as $key=>$value)
   print("<tr><td>$key</td>".
         "<td>$value</td></tr>");
?>
</table>
</body></html>
