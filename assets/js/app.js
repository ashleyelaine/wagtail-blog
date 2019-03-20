(function($) {
  // External Links [Wagtail doesn't add _blank target for external links]
  $('a[href^="http://"]').attr('target', '_blank');
  $('a[href^="https://"]').attr('target', '_blank');
})(jQuery);
