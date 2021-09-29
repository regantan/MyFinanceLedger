document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.hamburger_button').addEventListener('click', function() {
        document.querySelector('.hamburger_icon').classList.toggle('open');
        document.querySelector('.menu').classList.toggle('show');
    })
});