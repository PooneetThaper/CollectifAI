<?php
$uploadOk = 1;

// check if the inputted link is valid
$website = $_POST["url"];
if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
	echo "Invalid URL";
	$uploadOk = 1;
}

if ((substr($website, -4) != ".jpg") && (substr($website, -5) != ".jpeg")) {
	echo "Sorry, only JPG and JPEG files are allowed.";
	$uploadOk = 0;
}

// gets the index of the last occurrence of forward slash
$slashIndex = strrpos($website, "/", -4);
$imageName = substr($website, $slashIndex + 1);
copy($website, "uploads/" . $imageName);


echo "The file " . $imageName . " has been uploaded.";

// pass arguments as command line arguments
exec("../api.py a $imageName");

$uploadOk = 1;
?>