const body = document.getElementById("background");
function changecolor(e) {
    e.preventDefault();
    const redValue = document.getElementById("red").value;
    const greenValue = document.getElementById("green").value;
    const blueValue = document.getElementById("blue").value;
    body.style.backgroundColor = "rgb(" + redValue + "," + greenValue + "," + blueValue + ")";
}
