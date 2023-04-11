$("#loginModal").submit((e) => {
    e.preventDefault();
    if ($("#email").val() != "" && $("#password").val() != "") {
        $.ajax({
            url: '/api/login',
            type: 'post',
            data:
                { "email": $("#email").val(),
                    "password": $("#password").val()
                  },
            success: (response) => {
                location.reload();
            },
            error: (error) => {
                $(".hideAlert").css("display", "none");
                $("#alertAccountLoginAPIFailed").css("display", "block");
            }
        })
    }
    else {
        $(".hideAlert").css("display", "none");
        $("#alertAccountLoginFailed").css("display", "block");
    }
	}