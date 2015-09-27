$().ready(function(){
  $('.btn').click(function(event) {
    p = "Processing"
    $(event.currentTarget).html(p);
    setInterval(function() {
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
