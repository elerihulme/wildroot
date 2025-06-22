# Testing

## Manual Testing

| Page                | User Actions                                            | Expected Results                                                          | Y/N | Comments |
| ------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- | --- | -------- |
| Sign Up             |                                                         |                                                                           |     |          |
| 1                   | Open the Sign Up page                                   | Sign-up form is displayed                                                 | Y   |          |
| 2                   | Click the “Login” link in the form                      | Redirected to Log In page                                                 | Y   |          |
| 3                   | Enter a valid email address                             | Field accepts address in correct format                                   | Y   |          |
| 4                   | Enter a valid username                                  | Field accepts characters allowed for usernames                            | Y   |          |
| 5                   | Enter the password twice (matching)                     | Field validates password format and ensures both entries match            | Y   |          |
| 6                   | Click the “Sign Up” button                              | User is sent to email confirmation page and receives a confirmation email | Y   |          |
| 7                   | Confirm the email link                                  | Redirected to the Sign In page                                            | Y   |          |
| Log In              |                                                         |                                                                           |     |          |
| 1                   | Open the Log In page                                    | Log-in form is displayed                                                  | Y   |          |
| 2                   | Click the “Sign Up” link                                | Redirected to Sign Up page                                                | Y   |          |
| 3                   | Enter valid email                                       | Field only accepts valid email format                                     | Y   |          |
| 4                   | Enter valid password                                    | Field only accepts password format                                        | Y   |          |
| 5                   | Click the “Remember Me” checkbox                        | Browser remembers user credentials                                        | Y   |          |
| 6                   | Click the “Log In” button                               | Redirected to the site (user is authenticated)                            | Y   |          |
| 7                   | Click the “Logout” button                               | Redirected to Home page and user session ends                             | Y   |          |
| 8                   | Use browser Back button                                 | User remains logged out                                                   | Y   |          |
| Log Out             |                                                         |                                                                           |     |          |
| 1                   | Click the “Logout” link (when logged in)                | Redirects to home page and session is cleared                             | Y   |          |
| Navigation          |                                                         |                                                                           |     |          |
| 1                   | Click the logo                                          | Redirects to Home page                                                    | Y   |          |
| 2                   | Select “All Plants,” “Indoor,” or “Outdoor” links       | Product listing loads with the appropriate filter applied                 | Y   |          |
| 3                   | Click “My Garden” (while logged in)                     | Redirects to Garden page                                                  | Y   |          |
| 4                   | Click “Profile”                                         | Redirects to Profile page                                                 | Y   |          |
| Footer              |                                                         |                                                                           |     |          |
| 1                   | Click social media icons                                | Opens corresponding social site in new tab/window                         | Y   |          |
| Home                |                                                         |                                                                           |     |          |
| 1                   | Click “Shop Now” button                                 | Redirects to Products page                                                | Y   |          |
| 2                   | Click “Indoor Plants” or “Outdoor Plants” buttons       | Products page opens with indoor/outdoor filter preset                     | Y   |          |
| 3                   | Click “Explore My Garden” (logged in)                   | Redirects to Garden page                                                  | Y   |          |
| Products            |                                                         |                                                                           |     |          |
| 1                   | Apply sort and filter options                           | Product list updates with chosen sorting or filtering                     | Y   |          |
| 2                   | Use tag checkboxes (pet-friendly, air-purifying, shade) | Products matching the selected tags are displayed                         | Y   |          |
| 3                   | Clear filters                                           | All filters reset; full product list displayed                            | Y   |          |
| 4                   | Click a product card                                    | Redirects to Product Detail page                                          | Y   |          |
| Product Detail      |                                                         |                                                                           |     |          |
| 1                   | Adjust quantity with +/– buttons                        | Quantity field updates accordingly                                        | Y   |          |
| 2                   | Click “Add to Bag”                                      | Item is added to bag and success message shown                            | Y   |          |
| Bag                 |                                                         |                                                                           |     |          |
| 1                   | Increase/decrease item quantity                         | Bag updates item quantity and totals; decreasing to zero removes the item | Y   |          |
| 2                   | Click “Remove” button                                   | Item is removed from bag                                                  | Y   |          |
| 3                   | Click “Proceed to Checkout” when logged in              | Redirects to Checkout page                                                | Y   |          |
| 4                   | Click “Proceed to Checkout” when not logged in          | Button disabled and prompt instructs user to log in or sign up            | Y   |          |
| Checkout            |                                                         |                                                                           |     |          |
| 1                   | Fill out delivery form with valid details               | Form accepts data                                                         | Y   |          |
| 2                   | Check “Update profile with delivery information”        | Profile prepopulated on next checkout                                     | Y   |          |
| 3                   | Enter payment details and click “Pay Now”               | Payment processes and redirects to Checkout Success                       | Y   |          |
| Checkout Success    |                                                         |                                                                           |     |          |
| 1                   | View order confirmation page                            | Displays order number, email confirmation notice, and order summary       | Y   |          |
| 2                   | Click “Back to Profile” (if accessed from profile)      | Redirects to Profile page                                                 | Y   |          |
| Profile             |                                                         |                                                                           |     |          |
| 1                   | Update delivery information and submit                  | Success message confirms profile updated                                  | Y   |          |
| 2                   | Click an order number in order history                  | Redirects to details for that order (Order History page)                  | Y   |          |
| Order History       |                                                         |                                                                           |     |          |
| 1                   | Review past order details                               | Information for selected past order is displayed                          | Y   |          |
| Garden              |                                                         |                                                                           |     |          |
| 1                   | Click “Add Plant”                                       | Opens Add Garden Plant page                                               | Y   |          |
| 2                   | Click a plant in the list                               | Opens Garden Plant Detail page                                            | Y   |          |
| Garden Plant Detail |                                                         |                                                                           |     |          |
| 1                   | Click “Edit Plant”                                      | Opens Edit Garden Plant page                                              | Y   |          |
| 2                   | Click “Delete Plant,” confirm                           | Plant is removed from user’s garden                                       | Y   |          |
| Add Garden Plant    |                                                         |                                                                           |     |          |
| 1                   | Submit form with plant details and photo                | New plant is added to garden and photo saved                              | Y   |          |
| 2                   | Click “Cancel”                                          | Returns to Garden page without saving                                     | Y   |          |
| Edit Garden Plant   |                                                         |                                                                           |     |          |
| 1                   | Update plant details and submit                         | Changes saved and success message shown                                   | Y   |          |
| 2                   | Add another photo                                       | Additional photo appears in plant detail                                  | Y   |          |
| 3                   | Delete a photo                                          | Selected photo removed from plant                                         | Y   |          |
| Admin               |                                                         |                                                                           |     |          |
| 1                   | Navigate to `/admin/` and log in                        | Admin dashboard loads with management options for products and orders     | Y   |          |

## Bugs

**Solved bugs:**

1. I was getting an error message when I tried to test the JsonResponse response on Password change.

_Solution:_

**Unsolved bugs:**

1.

_Temporary Solution:_

_Future Solution:_

## Validation

### HTML Validation:

### CSS Validation:

### JS Validation:

### Python Validation:

---

## Lighthouse Report

LightHouse is a web performance testing tool that can be used to evaluate the performance of a website. The report is generated by Google Chrome.

[Lighthouse Report](documentation/testing/lighthouse_report.pdf)

---

## Compatibility

Testing was conducted on the following browsers;

-   Chrome;
-   Firefox;
-   Safari;

---

## Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

[Responsiveness Report](documentation/testing/responsiveness.pdf)

---
