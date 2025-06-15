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
