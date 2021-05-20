<?php

include_once('config.php');

$token = $config_token;
$email_filter = $config_email;

if (empty($_POST["email"])) {
    echo("Missing email");
    die();
}

$email = $_POST['email'];

// Remove all illegal characters from email
$email = filter_var($email, FILTER_SANITIZE_EMAIL);
$email_exploded = explode('@', $email);
$email_domain = array_pop($email_exploded);

// Validate e-mail
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo("Email invalid");
    die();
} else if ($email_domain != "student.uhasselt.be" && $email_domain != "uhasselt.be") {
    echo("Invalid UHasselt domain");
    die();
} 

// Verify Captcha
if (empty($_POST['g-recaptcha-response'])) {
    echo("Missing recaptcha response");
    die();
}

$post_data = http_build_query(
    array(
        'secret' => $config_recaptchakey,
        'response' => $_POST['g-recaptcha-response'],
        'remoteip' => $_SERVER['REMOTE_ADDR']
    )
);
$opts = array('http' =>
    array(
        'method'  => 'POST',
        'header'  => 'Content-type: application/x-www-form-urlencoded',
        'content' => $post_data
    )
);
$context  = stream_context_create($opts);
$response = file_get_contents('https://www.google.com/recaptcha/api/siteverify', false, $context);
$result = json_decode($response);
if (!$result->success) {
    echo("CAPTCHA verification failed");
    die();
}


if (!preg_match("/^security\.programmer(\+[^@]*)?@student\.uhasselt\.be$/i", $email)) {
    $array_data = [
        'from' => 'UH Student Portal <auth-ctf@ctf.edm.uhasselt.be>',
        'to' => $email,
        'subject' => 'UH-Student Portal 2FA Token',
        'text' => "Your 2FA code is: $token",
    ];

    $session = curl_init("https://api.eu.mailgun.net/v3/$config_maildomain/messages");
    curl_setopt($session, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    curl_setopt($session, CURLOPT_USERPWD, "api:$config_mailkey");
    curl_setopt($session, CURLOPT_POST, true);
    curl_setopt($session, CURLOPT_POSTFIELDS, $array_data);
    curl_setopt($session, CURLOPT_HEADER, false);
    curl_setopt($session, CURLOPT_ENCODING, 'UTF-8');
    curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($session, CURLOPT_SSL_VERIFYPEER, false);
    $response = curl_exec($session);
    curl_close($session);
}

echo("2FA mail sent");

?>