function decreaseQuantity(foodItemId) {
    var quantitySpan = document.getElementById('quantity' + foodItemId);
    var quantityInput = document.getElementById('quantityInput' + foodItemId);
    var currentQuantity = parseInt(quantitySpan.textContent);
    if (currentQuantity > 1) {
        quantitySpan.textContent = currentQuantity - 1;
        quantityInput.value = currentQuantity - 1;
    }
}

function increaseQuantity(foodItemId) {
    var quantitySpan = document.getElementById('quantity' + foodItemId);
    var quantityInput = document.getElementById('quantityInput' + foodItemId);
    var currentQuantity = parseInt(quantitySpan.textContent);
    quantitySpan.textContent = currentQuantity + 1;
    quantityInput.value = currentQuantity + 1;
}

    // Event listener for add to cart buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(function(addToCartBtn) {
        addToCartBtn.addEventListener('click', function(event) {
            const foodItemId = event.target.getAttribute('data-food-item-id');
            const quantity = document.querySelector(`#quantity${foodItemId}`).textContent;

            // Create a form element
            const form = document.createElement('form');
            form.method = 'post';
            form.action = '/add_to_cart/'; // Update the action attribute with your actual URL
            
            // Create input elements for food item id and quantity
            const foodItemIdInput = document.createElement('input');
            foodItemIdInput.type = 'hidden';
            foodItemIdInput.name = 'food_item_id';
            foodItemIdInput.value = foodItemId;
            form.appendChild(foodItemIdInput);
            
            const quantityInput = document.createElement('input');
            quantityInput.type = 'hidden';
            quantityInput.name = 'quantity';
            quantityInput.value = quantity;
            form.appendChild(quantityInput);

            // Append the form to the document body and submit it
            document.body.appendChild(form);
            form.submit();
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