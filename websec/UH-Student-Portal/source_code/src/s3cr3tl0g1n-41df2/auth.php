<?php

include_once('config.php');

if (!empty($_POST['pass']) && !empty($_POST['mail'])) {
    if (empty($_POST['2FA'])) {
        if ($_POST['pass'] === "123456" && $_POST['mail'] === $config_email) {
            echo "ok";
        } else {
            echo "wrong";
        }
    } else {
        if ($_POST['2FA'] === $config_token) {
            echo $config_flag;
        } else {
            echo "wrong";
        }
    }
} else {
    echo "incomplete";
}