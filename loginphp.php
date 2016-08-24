<?php
$servername = "mysql11.000webhost.com";
$username = "a8500552_bops";
$password = "webhost12345";
$dbname = "a8500552_employe";

$result=array();

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}



$user_id=$_REQUEST['user_id'];
$pass = $_REQUEST['pass'];


$sql = "Select user_id,password from employe where user_id='$user_id' and password='$pass'";

if ($conn->query($sql) === TRUE) {
	$result["success"]=1;
	echo json_encode($result);
} else {
	$result["success"]=0;
	echo json_encode($result);
}
	
$conn->close();
?> 
