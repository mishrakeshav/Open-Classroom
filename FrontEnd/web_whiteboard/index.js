context = document.getElementById('white_board').getContext("2d");
$('#white_board').mousedown(function (e) {
    var mouseX = e.pageX - this.offsetLeft;
    var mouseY = e.pageY - this.offsetTop;

    paint = true;
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
    redraw();
});
$('#white_board').mousemove(function (e) {
    if (paint) {
        addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
        redraw();
    }
});
$('#white_board').mouseup(function (e) {
    paint = false;
});
$('#white_board').mouseleave(function (e) {
    paint = false;
});
$('#choosePurpleSimpleColors').click(()=>{
    curColor = colorPurple;
})
$('#chooseGreenSimpleColors').click(()=>{
    curColor = colorGreen;
})
$('#chooseYellowSimpleColors').click(()=>{
    curColor = colorYellow;
})
$('#chooseBrownSimpleColors').click(()=>{
    curColor = colorBrown;
})
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var colorPurple = "#cb3594";
var colorGreen = "#659b41";
var colorYellow = "#ffcf33";
var colorBrown = "#986928";

var curColor = colorPurple;
var clickColor = new Array();
var paint;

function addClick(x, y, dragging) {
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
    clickColor.push(curColor);
}
function redraw() {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas

    // context.strokeStyle = "#df4b26";
    context.lineJoin = "round";
    context.lineWidth = $('#size').val(); // change the size of the stroke
    
    for (var i = 0; i < clickX.length; i++) {
        context.beginPath();
        if (clickDrag[i] && i) {
            context.moveTo(clickX[i - 1], clickY[i - 1]);
        } else {
            context.moveTo(clickX[i] - 1, clickY[i]);
        }
        context.lineTo(clickX[i], clickY[i]);
        context.closePath();
        context.strokeStyle = clickColor[i]
        context.stroke();
    }
}
$('#clear_complete').click(function () {
    let canvas = document.getElementById('white_board')
    clickX = [];
    clickY = [];
    clickDrag = [];
    context.clearRect(0, 0, canvas.width, canvas.height);
});
