const switchInput = document.querySelector('.switch input');
const babyContainers = document.querySelectorAll('.baby-container');
const svgIcon = document.querySelector('svg');

switchInput.addEventListener('change', function() {
    if (this.checked) {
        svgIcon.classList.add('rotateON');
        svgIcon.classList.remove('rotateOFF');
        babyContainers.forEach(container => {
            container.classList.add('active');
        });
    } else {
        svgIcon.classList.remove('rotateON');
        svgIcon.classList.add('rotateOFF');
        babyContainers.forEach(container => {
            container.classList.remove('active');
        });
    }
});
