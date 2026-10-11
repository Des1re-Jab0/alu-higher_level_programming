$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.com/';

  function translate() {
    const code = $('INPUT#language_code').val();

    $.get(url, { lang: code }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(translate);

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});