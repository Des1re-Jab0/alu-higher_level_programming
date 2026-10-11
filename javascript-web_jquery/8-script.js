const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  data.results.forEach(function (film) {
    $('UL#list_movies').append($('<li></li>').text(film.title));
  });
});