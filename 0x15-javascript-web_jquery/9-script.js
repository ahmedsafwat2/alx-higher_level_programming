
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  // console.log(data.hello)
  $('#hello').append('<p>' + data.hello + '</p>');
});
