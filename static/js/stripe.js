/**
 * Retrieve Stripe public key and client secret from hidden elements on the page.
 * Initialize the Stripe card element and handle form submission with secure payment intent.
 */

// Get Stripe public key and client secret from rendered DOM elements
var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
// Populate hidden input field for client secret
document.getElementById("client_secret_input").value = clientSecret;
// Initialise Stripe
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
// Define styling for card input fields
var style = {
    base: {
        color: "#000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#aab7c4",
        },
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545",
    },
};
// Create and mount the Stripe card element
var card = elements.create("card", { style: style });
card.mount("#card-element");

/**
 * Handle real-time validation errors from the Stripe card element.
 */
card.addEventListener("change", function (event) {
    var errorDiv = document.getElementById("card-errors");
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
});

// Get the form element
var form = document.getElementById("payment-form");
/**
 * Handle form submission by sending card and billing details to Stripe.
 * If payment is successful, the form is submitted. Otherwise, show the error.
 */
form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    // Disable card input and submit button to prevent multiple submissions
    card.update({ disabled: true });
    $("#submit-button").attr("disabled", true);
    $("#payment-form").fadeToggle(100);
    $("#payment-page").addClass("d-none");
    $("#loading-overlay").removeClass("d-none");

    // Get checkbox state and CSRF token
    var saveInfo = Boolean($("#id-save-info").attr("checked"));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Prepare data to be cached before confirming payment
    var postData = {
        csrfmiddlewaretoken: csrfToken,
        client_secret: clientSecret,
        save_info: saveInfo,
    };
    var url = "/checkout/cache_checkout_data/";

    /**
     * Send checkout data to cache view and then confirm card payment with Stripe.
     */
    $.post(url, postData)
        .done(function () {
            stripe
                .confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.full_name.value),
                            phone: $.trim(form.phone_number.value),
                            email: $.trim(form.email.value),
                            address: {
                                line1: $.trim(form.street_address1.value),
                                line2: $.trim(form.street_address2.value),
                                city: $.trim(form.town_or_city.value),
                                country: $.trim(form.country.value),
                                postal_code: $.trim(form.postcode.value),
                            },
                        },
                    },
                    shipping: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            postal_code: $.trim(form.postcode.value),
                        },
                    },
                })
                .then(function (result) {
                    if (result.error) {
                        // Display error message to user
                        var errorDiv = document.getElementById("card-errors");
                        var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                        $(errorDiv).html(html);
                        // Re-enable form and card input
                        $("#loading-overlay").addClass("d-none");
                        $("#payment-page").removeClass("d-none");
                        $("#payment-form").fadeToggle(100);
                        card.update({ disabled: false });
                        $("#submit-button").attr("disabled", false);
                    } else {
                        // Payment succeeded — submit the form
                        if (result.paymentIntent.status === "succeeded") {
                            form.submit();
                        }
                    }
                });
        })
        .fail(function () {
            // On error, reload the page so Django messages can display the issue
            location.reload();
        });
});
