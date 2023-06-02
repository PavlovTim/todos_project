
function handleClick() {
    alert("Вы нажали на кнопку");
    return 1
};

window.onload = function() {
    console.log('документ загрузился');

    document.getElementById(1).addEventListener('click', handleClick());
};