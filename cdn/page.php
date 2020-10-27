<?php include 'config.php' ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Image</title>
</head>

<style>
img {
    width: 200px;
    height: 200px;
}
</style>

<body>
    <img src="<?= 'http://servers.' . $config['domain'] . $_SERVER['REQUEST_URI'] ?>" alt="Requested image">
</body>
</html>