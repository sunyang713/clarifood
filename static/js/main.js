$().ready(function(){
  $('.btn').click(function(event) {
    setInterval(function() {
      var p = "Processing"
      setTimeout(function() {
        $(event.currentTarget).html(p + '.');
      }, 250);
      setTimeout(function() {
        $(event.currentTarget).html(p + '..');
      }, 500);
      setTimeout(function() {
        $(event.currentTarget).html(p + '...');
      }, 750);
      setTimeout(function() {
        $(event.currentTarget).html(p + '....');
      }, 1000);
    }, 1000);
  });

})

