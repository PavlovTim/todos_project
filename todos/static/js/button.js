
function handleClick() {
    alert("You complete a task!");
};

window.onload = function() {
    var buttons = document.getElementsByTagName("button")
    for(var i=0; i<buttons.length; i++) {
        buttons[i].addEventListener('click', handleClick)
    }
