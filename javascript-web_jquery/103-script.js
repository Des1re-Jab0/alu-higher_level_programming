$(document).ready(() => {
  const translate = () => {
    const langCode = $('#language_code').val();

    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + encodeURIComponent(langCode), (data) => {
      $('#hello').text(data.hello);
    });
  };

  $('#btn_translate').on('click', translate);

  $('#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      translate();
    }
  });
});
