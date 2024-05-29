
const $ = window.$;
$content = $('#list_movies');

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      // console.log(data.results)
      $.each(data.results, function (key, val) {
        $content.append('<li>' + val.title + '</li>');
      });
    }
  });
});
