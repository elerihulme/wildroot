// Get Stripe public key and client secret from the template context
let stripePublicKey = "{{ stripe_public_key }}";
let clientSecret = "{{ client_secret }}";

let stripe = Stripe(stripePublicKey);

// Set up Stripe.js and Elements to use in checkout form
let elements = stripe.elements();
let style = {
    base: {
        color: "#32325d",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#aab7c4",
        },
    },
    invalid: {
        color: "#fa755a",
        iconColor: "#fa755a",
    },
};

let card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle real-time validation errors from the card Element.
card.addEventListener("change", function (event) {
    let errorDiv = document.getElementById("card-errors");
    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submission
let form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
    ev.preventDefault();

    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value,
                    phone: form.phone_number.value,
                    email: form.email.value,
                    address: {
                        line1: form.street_address1.value,
                        line2: form.street_address2.value,
                        city: form.town_or_city.value,
                        postal_code: form.postcode.value,
                        country: form.country.value,
                    },
                },
            },
        })
        .then(function (result) {
            if (result.error) {
                // Show error to your customer (e.g., insufficient funds)
                let errorDiv = document.getElementById("card-errors");
                errorDiv.textContent = result.error.message;
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    form.submit(); // Submit the form
                }
            }
        });
});
