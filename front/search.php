<?php
$tag = $_POST["tag"];
// pass arguments as command line arguments
exec("../api.py f $tag");

// this piece of code is from w3schools
$myfile = fopen("out.txt", "r") or die("Unable to open file!");
// Output one line until end-of-file
while(!feof($myfile)) {
  echo fgets($myfile) . "<br>";
}
fclose($myfile);

?>