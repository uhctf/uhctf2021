1. Go to /robots.txt and find path to login panel
2. Find credentials in HTML attributes of the input fields
3. Log in with valid credentials
4. Notice that two requests are sent, to `auth.php` and `2fa.php`
5. Modify request to `2fa.php` to include YOUR email address (ending on `uhasselt.be`)
6. Receive 2FA token in your mailbox
7. Enter 2FA token