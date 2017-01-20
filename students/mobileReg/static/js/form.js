function showFlash(message) {
    $('#flash span').html(message);
    $('#flash').show();
}
$('#flash a').on('click', function(e) {
    e.preventDefault();
    $('#flash').hide();
});
$('form button').on('click', function(e) {
    e.preventDefault();

    var url = sendMessage == 'message' ? '/message';
    $.ajax(url, {
        method:'POST',
        dataType:'text',
        data:{
            to:$('#to').val()
        },
        success: function(data) {
            showFlash(data);
        },
        error: function(jqxhr) {
            alert('There was an error sending a request to the server :(');
        }
    })
});