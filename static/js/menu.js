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


// Get the added to cart message container
const addedToCartMessage = document.getElementById('addedToCartMessage');

// Function to display the added to cart message
function displayAddedToCartMessage() {
    addedToCartMessage.style.display = 'block';
    setTimeout(function() {
        addedToCartMessage.style.display = 'none';
    }, 10000); // Display message for 10 seconds
}

// Inside the event listener for the "ORDER NOW" button
document.querySelectorAll('.food-items button').forEach((button, index) => {
    button.addEventListener('click', function() {
        // Your existing code to handle adding item to cart
        
        // Display the added to cart message
        displayAddedToCartMessage();
    });
});
