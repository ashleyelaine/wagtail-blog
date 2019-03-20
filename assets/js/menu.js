(function($) {
  // Sub menu hovers
  $('.has-submenu').on({
    mouseenter: function() {
      if ($(window).width() >= 992) {
        $(this).find('.dropdown-menu').stop().slideDown(400);
        $(this).find('.dropdown-menu').css('z-index', '9999');
      }
    },
    mouseleave: function() {
      if ($(window).width() >= 992) {
        $(this).find('.dropdown-menu').stop().slideUp(400, function() {
          $(this).find('.dropdown-menu').css('z-index', '0');
        });
      }
    },
  });
})(jQuery);
