<?php

include("connect.PHP");
$id=$_GET['updateid'];
if(isset($_POST['update'])){
    $name=$_POST['username'];
    $email=$_POST['useremail'];
    $mobile=$_POST['mobilenumber'];
    $password=$_POST['password'];

    $sql="UPDATE `project` set id=$id,Name='$name',Email='$email',Mobile='$mobile',Password='$password' where id=$id";
    $result=mysqli_query($connect,$sql);
    if($result){
        header('location:display.php');
        // echo"updated sucessfully";
    }
    else{
        echo"data not updated";
    }


}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crud Operations</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
     <form  method="POST">
        Name:<br>
        <input type="text" id="my1" name="username" placeholder="Enter name"
        autocomplete="off"><br>
        Email:<br>
        <input type="email" id="my1"  name="useremail" placeholder="name@gmail.com"
        autocomplete="off"><br>
        Mobile:<br>
        <input type="number" id="my1"  name="mobilenumber" placeholder="Enter mobilenumber"
        autocomplete="off"><br>
        Password:<br>
        <input type="password" id="my1" name="password" autocomplete="off"><br>
        <input type="submit"  id="myde1" name="update"   value="Update"
        autocomplete="off">


</form>
    </div>
</body>
</html>