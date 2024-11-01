/* custom js */

document.addEventListener("DOMContentLoaded", function() {
    const toggleSwitch = document.getElementById('mode-toggle');

    toggleSwitch.addEventListener('change', function() {
        document.body.classList.toggle('dark-mode');
    });
});
