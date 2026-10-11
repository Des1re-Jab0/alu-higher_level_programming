$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
