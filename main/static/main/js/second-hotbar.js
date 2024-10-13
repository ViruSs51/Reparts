let lastScrollTop = 0;
const navbar = document.getElementById('hotbar');

navbar.classList.remove('second-hotbar-hidden');

window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        navbar.classList.add('second-hotbar-hidden');
    } else {
        navbar.classList.remove('second-hotbar-hidden');
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
