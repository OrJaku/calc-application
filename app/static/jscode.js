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

function drawDataURIOnCanvas() {
  var element = document.createElement('a');
  element.setAttribute('href', document.getElementById('Canvas').toDataURL('image/jpeg'));
  element.setAttribute('download', 'chart.jpeg');
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);

}


//function drawDataURIOnCanvas(strDataURI, Canvas) {
//    var img = new window.Image();
//    img.addEventListener("load", function () {
//        canvas.getContext("2d").drawImage(img, 0, 0);
//    });
//    img.setAttribute("src", strDataURI);
//    console.log(img)
//}

//function drawDataURIOnCanvas() {
//    var canvas = document.getElementById("canvas")
//    var context = canvas.getContext("2d")
//    var img = new Image()img.src = "./cat.jpg"img.onload = () => {  context.drawImage(img, 0, 0)
//
//}