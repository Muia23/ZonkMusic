$(document).ready(function(){         
    var movement = document.getElementsByClassName("show");
    var exit = document.getElementById("close");
    if (movement !== null) {
        exit.style.color = 'black';
    } else {
        exit.style.color = 'blue';
    }
})