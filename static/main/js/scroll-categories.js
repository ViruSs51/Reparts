document.addEventListener("DOMContentLoaded", function() {
    const categoryLists = document.querySelectorAll(".list-category");

    categoryLists.forEach(function(categoryList) {
        const buttonLeft = categoryList.previousElementSibling.querySelector("#category-button-left");
        const buttonRight = categoryList.previousElementSibling.querySelector("#category-button-right");
        const scrollAmount = 200;


        if (buttonLeft) {
            buttonLeft.addEventListener("click", function() {
                categoryList.scrollBy({
                    left: -scrollAmount,
                    behavior: 'smooth'
                });
            });
        }

        if (buttonRight) {
            buttonRight.addEventListener("click", function() {
                categoryList.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            });
        }
    });
});
