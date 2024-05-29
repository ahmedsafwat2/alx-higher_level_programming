
// $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
//     $('#character').text(data)
//     // console.log(data)
// })

// for style
const $ = window.$;
const $content = $('#character');

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      $content.text(data.name);
      // $.each(data, function(key, val){
      //     $content.append('<p>' + key + ':' + val +'</p>')
      // })
    }
  });
});
