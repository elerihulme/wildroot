function removeFromBag(itemId) {
    const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
    ).value;
    const url = `/bag/remove/${itemId}/`;

    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
    }).then((response) => {
        if (response.ok) {
            location.reload();
        } else {
            alert("Failed to remove item from bag.");
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".quantity-control").forEach((control) => {
        const minusBtn = control.querySelector(".minus-btn");
        const plusBtn = control.querySelector(".plus-btn");
        const display = control.querySelector(".quantity-display");
        const input = control.querySelector(".quantity-input");

        const updateButtons = (value) => {
            if (parseInt(value) <= 1) {
                minusBtn.disabled = true;
            } else {
                minusBtn.disabled = false;
            }
        };

        minusBtn.addEventListener("click", () => {
            let current = parseInt(input.value);
            if (current > 1) {
                current--;
                input.value = current;
                display.textContent = current;
                updateButtons(current);

                if (control.closest("form")?.action.includes("/bag/adjust/")) {
                    control.closest("form").submit();
                }
            }
        });

        plusBtn.addEventListener("click", () => {
            let current = parseInt(input.value);
            current++;
            input.value = current;
            display.textContent = current;
            updateButtons(current);

            if (control.closest("form")?.action.includes("/bag/adjust/")) {
                control.closest("form").submit();
            }
        });

        updateButtons(parseInt(input.value));
    });
});
