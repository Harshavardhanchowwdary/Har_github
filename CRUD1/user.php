<?php
include("connect.PHP");
if(isset($_POST['submit'])){
    $name=$_POST['username'];
    $email=$_POST['email'];
    $mobile=$_POST['number'];
    $password=$_POST['password'];
    $sql="INSERT INTO `project`(Name,Email,Mobile,password)
            values('$name','$email','$mobile','$password')";
    $result=mysqli_query($connect,$sql);
    if($result){
        header("location:display.php");
    }else{
        echo"not inserted";
    }

}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Operations</title>
    <link rel="stylesheet" href="style1.css">
</head>
<body>
    <form method="POST">
        Name:<br>
        <input type="text" name="username" placeholder="Enter your name"><br>
        Email:<br>
        <input type="email" name="email" placeholder="Enter your email"><br>
        Mobile:<br>
        <input type="number" name="number" placeholder="Enter your number"><br>
        Password:<br>
        <input type="password" id="p" name="password" ><br>
        <input type="submit" id="s" name="submit"  value="submit"><br>
    </form>


    
    
</body>
</html>