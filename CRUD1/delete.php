<?php

require("connect.PHP");
if(isset($_GET['deletedid'])){
    $id=$_GET['deletedid'];

    $sql="DELETE from `project` where id=$id";
    $result=mysqli_query($connect,$sql);
    if($result){
        header('location:display.php');
    }else{
        echo"data  not deleted";
    }
}

?>