$('.sidebar-button').on('click', function(e){
    e.preventDefault();
    $('.sidebar').toggleClass('active');
});