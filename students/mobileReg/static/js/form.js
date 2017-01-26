function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function showFlash(message) {
    $('#flash span').html(message);
    $('#flash').show();
}
$('#flash a').on('click', function(e) {
    e.preventDefault();
    $('#flash').hide();
});
    function send_pin() {
    var url = 'message/';
    $.ajax(url, {
                type: "POST",
                data: { phone:  $("#phone").val() },
            })
            .done(function(data) {
                showFlash("PIN sent via SMS!");
            })
            // .fail(function(jqXHR, textStatus, errorThrown) {
            //     alert(errorThrown + ' : ' + jqXHR.responseText);
            // });
}
