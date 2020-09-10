(function($) {
  $(document).ready(function () {
    let sending = false;
    const $submitRow = $('.submit-row')
    $('form').on('submit', function (event) {
      if (sending) {
        return false;
      }
      sending = true;
      $submitRow.addClass('submit-row-disabled');
      setTimeout(function () {
        sending = false;
        $submitRow.removeClass('submit-row-disabled');
      }, 10000);
      return true;
    });
  });
})(django.jQuery);
