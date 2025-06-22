# Features

## Navigation Bar

-   Mobile-friendly collapsible menu with a hamburger button and site logo at the center.

-   Links to Home, All Plants, Indoor, Outdoor, My Garden, Profile, Login/Sign Up or Logout based on authentication state.

-   Basket icon leading to the bag page.

-   UK‑only delivery banner displayed below the navbar on each page via a template block.

## Footer

-   Social media icons for Instagram, X/Twitter, Facebook and Pinterest that open in a new tab.

-   Copyright notice displayed at the bottom.

## Home Page

-   Hero section with tagline, “Shop Now” button and responsive full-width background image.

-   Sections describing the mission, reasons to choose the shop and browse categories buttons for indoor/outdoor plants.

-   “My Garden” call‑to‑action encouraging users to visit their garden page.

## Authenitication

-   Sign‑up page linking to the login page if the user already has an account, includes a form for account creation.

-   Log‑in page with link to sign up for new users and form submission for authentication.

-   Log‑out page confirming the user wants to sign out with a simple form button.

## Products Page

-   Filter and sort controls (environment, category, difficulty, tags) with an Apply/Clear option.

-   Product grid displaying image, name, price and tags; each card links to the product detail page.

-   Pagination navigation and a “Go to top” button shown after scrolling.

## Product Detail Page

-   Large product image with information such as botanical name, price, description and care requirements.

-   Quantity increment/decrement controls and “Add to Bag” button handled by JavaScript.

## Shopping Bag

-   Responsive table listing selected products, quantity controls, item totals and a remove button.

-   Bag total and “Proceed to Checkout” button enabled only for logged‑in users; guests are prompted to log in or sign up.

-   Message and “Keep Shopping” button shown when the bag is empty.

## Checkout

-   Summary of bag items with subtotals and delivery cost on the left and a delivery/payment form on the right.

-   Save-info checkbox to store delivery details and Stripe integration for payment processing with a loading overlay during submission.

## Checkout Success

-   Order confirmation page displaying order number, delivery address and order details with a link back to Profile or Home.

## Profile

-   Form to update saved delivery information and an order history table showing past orders with links to view each order again.

## Order History

-   Past order details are displayed using the same checkout success template when accessed from the profile section (handled by order_history view).

## Garden

-   Authenticated users see a grid of their plants with “Add Plant” button

-   Unauthenticated users are prompted to log in or sign up.

## Garden Plant Detail

-   Plant details page with edit and delete options plus a photo carousel if multiple images are present.

-   Confirmation modal for deleting a plant.

## Add/Edit Garden Plant

-   Form for creating or editing a plant record with a separate section to upload a photo and manage existing photos when editing.

## Admin

-   Standard Django admin site available at /admin/ for managing products, orders and garden entries.

## 404 Page

-   Custom 404 page that displays a friendly message and a button linking back to the home page.

## Responsive Features

-   Bootstrap’s grid and navbar-toggler enable navigation and layout changes on smaller screens (e.g., collapsible menu on mobile).

-   Tables within the shopping bag and profile order history are wrapped in table-responsive containers for mobile viewing.

-   Product cards and garden plant cards adjust across screen widths via responsive column classes (col-md-6 col-lg-4) in the templates.
