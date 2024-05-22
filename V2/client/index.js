function saveIpAndRedirect() {
    const ip = document.getElementById('arduinoIp').value;
    if (ip) {
        localStorage.setItem('arduinoIp', ip);
        window.location.href = 'control.html';
    } else { 
        alert('Please enter a valid IP address');
    }
}
