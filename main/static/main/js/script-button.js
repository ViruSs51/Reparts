

function toggleMenu() {
    var menu = document.getElementById('menu-content');
    menu.classList.toggle('open');
}

document.getElementById('menu-button-outer').addEventListener('click', function(e) {
    e.preventDefault();
    toggleMenu();
});

document.getElementById('menu-button-inner').addEventListener('click', function(e) {
    e.preventDefault();
    toggleMenu();
});