$(document).ready(function () {

  const url = 'https://hellosalut.stefanbohacek.com/';

  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();

    $.get(url, { lang: code }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
