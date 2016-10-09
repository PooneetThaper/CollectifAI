<?php
$tag = $_POST["tag"];
// pass arguments as command line arguments
exec("../api.py f $tag");
?>