const apiDataContainers = document.querySelectorAll('.api-data');

async function updateData() {
    console.log("Updating data");
    const res = await fetch('/api/data');
    const data = await res.json();
    apiDataContainers.forEach((container) => {
        const key = container.getAttribute('data-api-id');
        container.textContent = data[key];
    });
}

dataUpdater = setInterval(updateData, 3000);
