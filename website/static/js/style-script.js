const switchInput = document.querySelector('.switch input');
const babyContainers = document.querySelectorAll('.baby-container');
const titleC = document.querySelectorAll('.titleC');
const number = document.querySelectorAll('.number');
const svgIcon = document.querySelector('svg');

switchInput.addEventListener('change', async function() {
    const power = this.checked ? 1 : 0;
    try {
        const response = await fetch('/api/power', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "power": power })
        });

        if (!response.ok) {
            throw new Error('Failed to update LED value');
        }

        if (this.checked) {
            svgIcon.classList.add('rotateON');
            svgIcon.classList.remove('rotateOFF');
            babyContainers.forEach(container => container.classList.add('active'));
            titleC.forEach(element => element.classList.remove('hidden'));
            number.forEach(element => element.classList.remove('hidden'));
        } else {
            svgIcon.classList.remove('rotateON');
            svgIcon.classList.add('rotateOFF');
            babyContainers.forEach(container => container.classList.remove('active'));
            titleC.forEach(element => element.classList.add('hidden'));
            number.forEach(element => element.classList.add('hidden'));
        }
    } catch (error) {
        console.error('Error updating LED value:', error);
    }
});

