$(document).ready(() => {
  $('#btn_translate').on('click', () => {
    const langCode = $('#language_code').val();

    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + encodeURIComponent(langCode), (data) => {
      $('#hello').text(data.hello);
    });
  });
});
