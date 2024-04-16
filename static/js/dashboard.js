const overlay = document.getElementById('overlay');
const popup = document.querySelector('.popup');
const closeButton = document.querySelector('.close');
const navBar = document.querySelector('nav');

function showPopup() {
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.6)';
    popup.style.display = 'block';
    navBar.style.backgroundColor = 'rgba(255, 255, 255, 0.3)'; 
}

function hidePopup() {
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0)';
    popup.style.display = 'none';
    navBar.style.backgroundColor = 'rgba(255, 255, 255, 0.9)'; 
}

closeButton.addEventListener('click', hidePopup);

window.onload = function() {
    setTimeout(showPopup, 1000);

    closeButton.addEventListener('click', hidePopup);
}

