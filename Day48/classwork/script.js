age = prompt("Enter your age:")

if (age < 18){
    console.log(age, "ბილეთის ფასი არის 10 ლარი")
} else if (age <= 65){
    console.log(age, "ბილეთის ფასი არის 20 ლარი")
} else {
    console.log(age, 'ბილეთის ფასი არის 15 ლარი')
}