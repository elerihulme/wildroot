/**
 * Sends a POST request to remove an item from the shopping bag.
 * Reloads the page on success, shows an alert on failure.
 */
function removeFromBag(itemId) {
    // Get CSRF token from the page for security
    const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
    ).value;
    // Build the URL for the remove request
    const url = `/bag/remove/${itemId}/`;

    // Send the POST request to remove the item
    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
    }).then((response) => {
        // If the request is successful, reload the page to update the bag
        if (response.ok) {
            location.reload();
        } else {
            // Show an alert if the item could not be removed
            alert("Failed to remove item from bag.");
        }
    });
}

/**
 * Adds quantity control logic for all quantity input groups on the page.
 * Allows increasing and decreasing quantity and submits the form on change.
 */
document.addEventListener("DOMContentLoaded", () => {
    // Select all quantity control elements on the page
    document.querySelectorAll(".quantity-control").forEach((control) => {
        // Get the minus button, plus button, display element, and input field
        const minusBtn = control.querySelector(".minus-btn");
        const plusBtn = control.querySelector(".plus-btn");
        const display = control.querySelector(".quantity-display");
        const input = control.querySelector(".quantity-input");

        // Function to enable or disable the minus button based on quantity
        const updateButtons = (value) => {
            if (parseInt(value) <= 1) {
                minusBtn.disabled = true;
            } else {
                minusBtn.disabled = false;
            }
        };

        // Event listener for minus button click
        minusBtn.addEventListener("click", () => {
            let current = parseInt(input.value);
            if (current > 1) {
                current--;
                input.value = current;
                display.textContent = current;
                updateButtons(current);

                // Submit the form automatically if it's from the bag adjustment page
                if (control.closest("form")?.action.includes("/bag/adjust/")) {
                    control.closest("form").submit();
                }
            }
        });

        // Event listener for plus button click
        plusBtn.addEventListener("click", () => {
            let current = parseInt(input.value);
            current++;
            input.value = current;
            display.textContent = current;
            updateButtons(current);

            // Submit the form automatically if it's from the bag adjustment page
            if (control.closest("form")?.action.includes("/bag/adjust/")) {
                control.closest("form").submit();
            }
        });

        // Initialize button state on page load
        updateButtons(parseInt(input.value));
    });
});
