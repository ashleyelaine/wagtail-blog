(function($) {
  // EXTERNAL LINKS
  setTimeout(function() {
    $('a[target="_blank"]').addClass('external-link');
    $('.external-link').append(' <span class="sr-only"> Opens in new window</span>');
  }, 100);

  // DROPDOWN MENUS
  $('.allow-toggle').focusin(function() {
    console.log('focust in');
    $(this).parents('.has-submenu').find('.dropdown-menu').css('display', 'block');
  });

  $('.dropdown-menu li:last-of-type .menu-link').focusout(function() {
    console.log('focust in');
    $(this).parents('.dropdown-menu').css('display', 'none');
  });
})(jQuery);

// RECOGNIZE A KEYBOARD USER
function handleFirstTab(e) {
  if (e.keyCode === 9) { // the "I am a keyboard user" key
      document.body.classList.add('user-is-tabbing');
      window.removeEventListener('keydown', handleFirstTab);
  }
}

window.addEventListener('keydown', handleFirstTab);
