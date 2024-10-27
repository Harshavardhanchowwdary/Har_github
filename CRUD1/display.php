<?php

require("connect.PHP");
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Operations</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <button class="hars"><a href="user.php">Add User</a></button>
        <center><table class="table" cellspacing='12px'  cellpadding='7px' border="5px"></center>
  <thead>
    <tr>
      <th scope="col">Sl No</th>
      <th scope="col">Name</th>
      <th scope="col">Email</th>
      <th scope="col">Mobilenumber</th>
      <th scope="col">Password</th>
      <th scope="col" id="1">Operations</th>
    </tr>
  </thead>
  <tbody>
    <?php
    $sql="SELECT *from `project`";
    $result=mysqli_query($connect,$sql);
    if($result){
      while($row=mysqli_fetch_assoc($result)){
        $id=$row['id'];
        $name=$row['Name'];
        $email=$row['Email'];
        $mobile=$row['Mobile'];
        $password=$row['password'];
      
      echo"<tr>
      <th scope='row'>$id</th>
      <td>$name</td>
      <td>$email</td>
      <td>$mobile</td>
      <td>$password</td>
      <td>
      <button id='h'><a href='delete.php? deletedid=$id'>Delete</a></button>
      <button id='a'><a href='update.php? updateid=$id' >Update</a></button>
      </td>
      <tr>";
      }
    }
    ?>

</table>

    
    </div>
    
</body>
</html>