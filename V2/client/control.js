const arduinoIp = localStorage.getItem('arduinoIp');
if (!arduinoIp) {
    alert('Arduino IP not set. Redirecting to IP entry page.');
    window.location.href = 'index.html';
}

function updateAngle(joint, angle) {
    document.getElementById(`${joint}Value`).innerText = angle;
    
    const url = `http://${arduinoIp}/move?joint=${joint}&angle=${angle}`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                console.log(`${joint} moved to angle ${angle}`);
            } else {
                console.error(`Error moving ${joint}`);
            }
        })
        .catch(error => console.error('Error:', error));
}
