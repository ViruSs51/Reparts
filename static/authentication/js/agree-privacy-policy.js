const checkbox = document.getElementById('agree');
const submitBtn = document.getElementById('submit-btn');

checkbox.addEventListener('change', function() {
    submitBtn.disabled = !this.checked;
});