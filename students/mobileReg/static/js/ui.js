var sendMessage = 'message';

$('#messaging').on('click', function(e) { 
    e.preventDefault();
    changeTab('message');
});

$('#flash a').on('click', function(e) {
    e.preventDefault();
    $('#flash').hide();
});