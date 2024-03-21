const switchInput = document.querySelector('.switch input');
const babyContainers = document.querySelectorAll('.baby-container');
const titleC = document.querySelectorAll('.titleC');
const number = document.querySelectorAll('.number');
const svgIcon = document.querySelector('svg');

switchInput.addEventListener('change', function() {
    if (this.checked) {
        svgIcon.classList.add('rotateON');
        svgIcon.classList.remove('rotateOFF');
        babyContainers.forEach(container => {
            container.classList.add('active');
        });
        titleC.forEach(element => {
            element.classList.remove('hidden');
        });
        number.forEach(element => {
            element.classList.remove('hidden');
        });
    } else {
        svgIcon.classList.remove('rotateON');
        svgIcon.classList.add('rotateOFF');
        babyContainers.forEach(container => {
            container.classList.remove('active');
        });
        titleC.forEach(element => {
            element.classList.add('hidden');
        });
        number.forEach(element => {
            element.classList.add('hidden');
        });
    }
});
