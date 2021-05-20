function verifyAuth(token) {
    let payload = {
        email: $('#mail').val(),
        "g-recaptcha-response": token,
    };
    $.post("/s3cr3tl0g1n-41df2/2fa.php",
    payload,
    function(data,status){});
}
(function($) {
    "use strict";
    var input = $('.validate-input .input100');
    $('.validate-form').on('submit', function(e) {
        e.preventDefault();
        $('#msg').text("");
        let payload = {
            mail: $('#mail').val(),
            pass: $('#pass').val(),
        };
        if ($('#2fa').val().length > 0) {
            payload['2FA'] = $('#2fa').val();
        }
        $.post("/s3cr3tl0g1n-41df2/auth.php",
        payload,
        function(data,status){
        if (data !== "ok") {
            $('#msg').text(data);
        } else {
            let captchaval = grecaptcha.execute();
            $("#2fa-container").show();
        }
        });
    });
})(jQuery);
