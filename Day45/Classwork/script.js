let userInput = document.getElementById("name")
let output = document.getElementById("output")
function login(event) {
    event.preventDefault()
    output.textContent = "Your name is: " + userInput.value
}


/* რომ შევქმნათ ფუნქცია გვწირდება function */