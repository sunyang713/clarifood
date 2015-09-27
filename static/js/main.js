$(function(){

    // $('a, button').click(function() {
    //     $(this).toggleClass('active');
    // });

    $('.submit').click(function(event) {
		$(event.currentTarget).html('Processing...');
	});

});
