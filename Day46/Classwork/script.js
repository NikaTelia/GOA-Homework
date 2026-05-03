const body = document.getElementById("Screen");

function changecolor(e) {
    e.preventDefault();

    const redValue = document.getElementById("red").value;
    const greenValue = document.getElementById("green").value;
    const blueValue = document.getElementById("blue").value;

    body.style.backgroundColor = "rgb(" + redValue + "," + greenValue + "," + blueValue + ")";
}


let answer = Math.pow(10, 3);
console.log(answer);

// math.round - დაამგვალებს მთლადს
// math.floor -  დაამგვალებს ქვემოთ
// math.ceil - დაამგვალებს ზემოთ
// math.random - რანდომ ციფრს ამოიტანს (0-დან 1-მდე)
// math.pow(a, b) -- ხარხში აყვანა
// math.pi - რიცხვის პი აჩვენებს (3.14...)