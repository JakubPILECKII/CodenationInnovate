

let myName ="Jakub"; // Variable declaration for a mutable variable (CAB VE CHANGED)
const myLastName ="12345"; // veriabel declaraction for inmmutable variable (Cant be changed)


function myFunction (num1, num2) {
    let result = num1 + num2
    return result
};

function hider () {
    let element = document.getElementsById("task-box");
    element.classList.toggle("hidden")
}

function darkMode () {
    let element = document.getElementById("base-body")
    element.classList.toggle("dark-mode")
}
