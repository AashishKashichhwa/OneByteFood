// Get the quantity span and buttons for each food item
const quantitySpans = document.querySelectorAll('.quantity');
const decreaseBtns = document.querySelectorAll('.decrease');
const increaseBtns = document.querySelectorAll('.increase');

// Set initial quantity for each food item
let quantities = Array.from({ length: quantitySpans.length }, () => 1);

// Event listeners for each set of buttons
decreaseBtns.forEach((btn, index) => {
    btn.addEventListener('click', function() {
        if (quantities[index] > 1) {
            quantities[index]--;
            quantitySpans[index].textContent = quantities[index];
        }
    });
});

increaseBtns.forEach((btn, index) => {
    btn.addEventListener('click', function() {
        quantities[index]++;
        quantitySpans[index].textContent = quantities[index];
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var cartOverlay = document.getElementById("cart-overlay");
    var addToCartButtons = document.querySelectorAll(".add-to-cart-btn");

    // Function to toggle cart overlay visibility
    function toggleCartOverlay() {
        cartOverlay.classList.toggle("show");
    }

    // Function to display "Added to cart" message for a specific button
    function displayAddedToCartMessage(button) {
        var addedToCartMessage = button.nextElementSibling;
        addedToCartMessage.style.display = "block";
        setTimeout(function() {
            addedToCartMessage.style.display = "none";
        }, 3000); // Hide message after 3 seconds
    }

    // Event listener for each "Add to Cart" button
    addToCartButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            toggleCartOverlay();
            displayAddedToCartMessage(button);
        });
    });

    // Close cart overlay when clicking outside of it
    window.addEventListener("click", function(event) {
        if (event.target === cartOverlay) {
            toggleCartOverlay();
        }
    });
});