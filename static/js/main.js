$(function(){
	console.log('happening!!')
    $('a, button').click(function() {
        $(this).toggleClass('active');
    });
});

