const buttonIds = ['menu-button', 'in-menu-button'];
const menu = document.getElementById('menu');

buttonIds.forEach(id => {
    document.getElementById(id).addEventListener('click', () => {
        menu.classList.toggle('open');
        document.body.classList.toggle('no-scroll');
    });
});
