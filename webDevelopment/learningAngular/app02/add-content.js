$(function() {
    //$('p#p1').text('test');
    $('h1').hide().fadeIn(3000);
    // button 1 click action
    $('#btn1').on('click', function() {
        var msg = getMess();
        $('#p1').text(msg);
    });
});

function getMess() {

    return 'Hi, Bacchus'
}