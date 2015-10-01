$().ready(function(){
  $('.btn').click(function(event) {
    var p = "Processing"
    $(event.currentTarget).html(p);
    setInterval(function(){
      $(event.currentTarget).html(p += '.');
    }, 1000);
  });

})
