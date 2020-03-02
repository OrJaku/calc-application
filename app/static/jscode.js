var mousePressed = false;
var lastX, lastY;
var ctx;

function InitThis() {
    ctx = document.getElementById('Canvas').getContext("2d");

    $('#Canvas').mousedown(function (e) {
        mousePressed = true;
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
    });

    $('#Canvas').mousemove(function (e) {
        if (mousePressed) {
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
        }
    });

    $('#Canvas').mouseup(function (e) {
        mousePressed = false;
    });
	    $('#Canvas').mouseleave(function (e) {
        mousePressed = false;
    });
}

function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = $('#selColor').val();
        ctx.lineWidth = $('#selWidth').val();
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x; lastY = y;
}

function clearArea() {
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

//function drawDataURIOnCanvas() {
//  var element = document.createElement('a');
//  element.setAttribute('href', document.getElementById('Canvas').toDataURL('image/jpeg'));
//  element.setAttribute('download', 'chart.jpeg');
//  element.style.display = 'none';
//  document.body.appendChild(element);
//  element.click();
//  document.body.removeChild(element);
//  return element
//
//}
function drawDataURIOnCanvas() {
  var element = document.createElement('a');
  element.setAttribute('href', document.getElementById('Canvas').toDataURL('image/jpeg'));
  element.setAttribute('download', 'chart.jpeg');
  element.style.display = 'none';
  $.ajax({
        url: 'image', // point to server-side URL
        dataType: 'jpeg', // what to expect back from server
        cache: false,
        contentType: false,
        processData: false,
        data: form_data,
        type: 'post',
        success: function (response) { // display success response
            $('#msg').html('');
            $.each(response, function (key, data) {
                if(key !== 'message') {
                    $('#msg').append(key + ' -> ' + data + '<br/>');
                } else {
                    $('#msg').append(data + '<br/>');
                }
            })
        },
        error: function (response) {
						$('#msg').html(response.message); // display error response

  }

//function drawDataURIOnCanvas() {
//    var canvas = document.getElementById("canvas")
//    var context = canvas.getContext("2d")
//    var img = new Image()img.src = "./cat.jpg"img.onload = () => {  context.drawImage(img, 0, 0)
//
//}