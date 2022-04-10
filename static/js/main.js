
$('.spinner-border').hide();

$('form').on('submit', function(event) {
    $('#res').hide();
    $('.spinner-border').fadeIn();
    $.ajax({
        data : {
            sl : $('#in1').val(),
            sw : $('#in2').val(),
            pl : $('#in3').val(),
            pw : $('#in4').val()
        },
        type : 'POST',
        url : '/process'
    })
    .done(function(data) {
        if (data.error) {
            $('.spinner-border').fadeOut();
            $('#res').text(data.error).show();
            
        }
        else {
            $('.spinner-border').fadeOut();
            $('#res').text("The predicted flower type is : " + data.pred).show();
            
            
        }
        
        
    });

    event.preventDefault();

});