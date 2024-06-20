document.addEventListener('DOMContentLoaded', function() {
    // Script to handle the progress bar on button click
    const upgradeButton = document.getElementById('upgradeButton');
    const progressBar = document.getElementById('progressBar');

    upgradeButton.addEventListener('click', function() {
        let width = 0;
        const interval = setInterval(function() {
            if (width >= 100) {
                clearInterval(interval);
            } else {
                width += 1; // Adjust the increment for speed
                progressBar.style.width = width + '%';
            }
        }, 5000); // Adjust speed of progress bar here (milliseconds)
    });
});
