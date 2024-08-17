let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
const fixedElement = document.getElementById('hotbar_4');
const menuElement = document.getElementById('menu-content');

function handleScroll(scrollTop) {
    if (scrollTop > lastScrollTop) {
        // Scrolling down
        fixedElement.style.transform = 'translateY(100%)';
    } else {
        // Scrolling up
        fixedElement.style.transform = 'translateY(0)';
    }
    lastScrollTop = scrollTop;
}

// Handle scroll on the window (main page)
window.addEventListener('scroll', function() {
    handleScroll(window.pageYOffset || document.documentElement.scrollTop);
});

// Handle scroll on the menu element
menuElement.addEventListener('scroll', function() {
    handleScroll(menuElement.scrollTop);
});
