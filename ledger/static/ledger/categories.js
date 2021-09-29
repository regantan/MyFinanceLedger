document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.new_category_button').addEventListener('click', () => {
        console.log('Button Clicked!');
        document.querySelector('.new_category_form').classList.toggle('show');
    })
})