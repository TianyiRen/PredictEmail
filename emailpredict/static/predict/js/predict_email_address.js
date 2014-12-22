$(document).ready(function () {
    $('.verify_btn').click(function () {
        var full_name = $(this).parent().siblings(":first").text();
        var email = $(this).parent().siblings(":nth-child(2)").text();
        $.ajax({
            url: "/verify_email_ajax",
            dataType: "json",
            data: {
                full_name: full_name,
                email: email,
            },
            success: function(data) {
                if (data.verified) {
                    location.reload();
                }
            }
        });
    });
});