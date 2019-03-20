(function($) {
  // FAQ accordian
  $('.accordian-handle').click(function() {
    $('.drawer-content').slideUp();
    $(this).parent('.accordian').find('.drawer-content').stop(true, false).slideToggle();
    if ($(this).hasClass('active')) {
      $(this).toggleClass('active');
      $(this).find('.icon').toggleClass('active');
    } else {
      $('.accordian-handle.active, .icon.active').removeClass('active');
      $(this).addClass('active');
      $(this).find('.icon').addClass('active');
    }
  });
})(jQuery);
