<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include '../config.php';

$uri = $_SERVER['REQUEST_URI'];

$pdo = new PDO('mysql:host='.$config['db']['host'] . ';dbname=' . $config['db']['dbname'] . ';charset=utf8', $config['db']['user'], $config['db']['password']);

$sql = $pdo->prepare('SELECT filename, server FROM images WHERE filename=:filename');
$sql->execute([
    'filename' => substr($uri, 1),
]);

$img = $sql->fetch();
if ($img) {
    http_response_code(301);
    header('Location: ' . 'http://' . $img['server'] . '.' . $config['domain'] . $uri);
} else {
    http_response_code(404);
}