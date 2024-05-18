const overlay = document.getElementById('overlay');
const popup = document.querySelector('.popup');
const closeButton = document.querySelector('.close');
const navBar = document.querySelector('nav');

function showPopup() {
    overlay.style.display = 'block'; // Show the overlay
    popup.style.display = 'block'; // Show the popup
    navBar.classList.add('nav-disabled'); // Disable nav bar
    navBar.style.backgroundColor = 'rgba(255, 255, 255, 0.3)'; 
}

function hidePopup() {
    overlay.style.display = 'none'; // Hide the overlay
    popup.style.display = 'none'; // Hide the popup
    navBar.classList.remove('nav-disabled'); // Enable nav bar
    navBar.style.backgroundColor = 'rgba(255, 255, 255, 0.9)'; 
}

closeButton.addEventListener('click', hidePopup);

window.onload = function() {
    setTimeout(showPopup, 1000);
}
