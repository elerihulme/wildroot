# Testing

## Manual Testing

| Page                   | User Actions                                            | Expected Results                                                                                                 | Y/N | Comments |
| ---------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --- | -------- |
| Sign Up                |                                                         |                                                                                                                  |     |          |
| 1                      | Open the Sign Up page                                   | Sign-up form is displayed                                                                                        | Y   |          |
| 2                      | Click the “Login” link in the form                      | Redirected to Log In page                                                                                        | Y   |          |
| 3                      | Enter a valid email address                             | Field accepts address in correct format                                                                          | Y   |          |
| 4                      | Enter a valid username                                  | Field accepts characters allowed for usernames                                                                   | Y   |          |
| 5                      | Enter the password twice (matching)                     | Field validates password format and ensures both entries match                                                   | Y   |          |
| 6                      | Click the “Sign Up” button                              | User is sent to email confirmation page and receives a confirmation email                                        | Y   |          |
| 7                      | Confirm the email link                                  | Redirected to the Sign In page                                                                                   | Y   |          |
| Log In                 |                                                         |                                                                                                                  |     |          |
| 1                      | Open the Log In page                                    | Log-in form is displayed                                                                                         | Y   |          |
| 2                      | Click the “Sign Up” link                                | Redirected to Sign Up page                                                                                       | Y   |          |
| 3                      | Enter valid email                                       | Field only accepts valid email format                                                                            | Y   |          |
| 4                      | Enter valid password                                    | Field only accepts password format                                                                               | Y   |          |
| 5                      | Click the “Remember Me” checkbox                        | Browser remembers user credentials                                                                               | Y   |          |
| 6                      | Click the “Log In” button                               | Redirected to the site (user is authenticated)                                                                   | Y   |          |
| Log Out                |                                                         |                                                                                                                  |     |          |
| 1                      | Click the “Logout” button                               | Redirected to Home page and user session ends                                                                    | Y   |          |
| 2                      | Use browser Back button                                 | User remains logged out                                                                                          | Y   |          |
| Navigation             |                                                         |                                                                                                                  |     |          |
| 1                      | Click the logo                                          | Redirects to Home page                                                                                           | Y   |          |
| 2                      | Select “All Plants,” “Indoor,” or “Outdoor” links       | Product listing loads with the appropriate filter applied                                                        | Y   |          |
| 3                      | Click "Bag" icon                                        | Redirects to the Shopping Bag Page                                                                               | Y   |          |
| If Logged In:          |                                                         |                                                                                                                  |     |          |
| 4                      | Click “My Garden”                                       | Redirects to Garden page                                                                                         | Y   |          |
| 5                      | Click “Profile”                                         | Redirects to Profile page                                                                                        | Y   |          |
| 6                      | Click "Logout"                                          | Redirects to Log Out page                                                                                        | Y   |          |
| If Logged Out:         |                                                         |                                                                                                                  |     |          |
| 7                      | Click "Sign Up"                                         | Redirects to Sign Up page                                                                                        | Y   |          |
| Footer                 |                                                         |                                                                                                                  |     |          |
| 1                      | Click social media icons                                | Opens corresponding social site in new tab/window                                                                | Y   |          |
| Home                   |                                                         |                                                                                                                  |     |          |
| 1                      | Click “Shop Now” button                                 | Redirects to Products page                                                                                       | Y   |          |
| 2                      | Click “Indoor Plants” or “Outdoor Plants” buttons       | Products page opens with indoor/outdoor filter preset                                                            | Y   |          |
| 3                      | Click “Explore My Garden”                               | Redirects to Garden page                                                                                         | Y   |          |
| Products               |                                                         |                                                                                                                  |     |          |
| 1                      | Apply sort and filter options                           | Product list updates with chosen sorting or filtering                                                            | Y   |          |
| 2                      | Use tag checkboxes (pet-friendly, air-purifying, shade) | Products matching the selected tags are displayed                                                                | Y   |          |
| 3                      | Clear filters                                           | All filters reset; full product list displayed                                                                   | Y   |          |
| 4                      | Click a product card                                    | Redirects to Product Detail page                                                                                 | Y   |          |
| 5                      | Click a pagination buttons                              | Displays next or previous page of products                                                                       | Y   |          |
| Product Detail         |                                                         |                                                                                                                  |     |          |
| 1                      | Adjust quantity with +/– buttons                        | Quantity field updates accordingly                                                                               | Y   |          |
| 2                      | Click “Add to Bag”                                      | Item is added to bag and success message shown                                                                   | Y   |          |
| 3                      | Click “Back to Products”                                | Redirects to product list page with any previous filters still applied                                           | Y   |          |
| Bag                    |                                                         |                                                                                                                  |     |          |
| If Items in Bag:       |                                                         |                                                                                                                  |     |          |
| 1                      | View Shopping Bag                                       | Displays table of current items in user's bag                                                                    | Y   |          |
| 2                      | Click to increase/decrease item quantity                | Bag updates item quantity and totals; decreasing to zero removes the item                                        | Y   |          |
| 3                      | Click “Remove” button                                   | Item is removed from bag                                                                                         | Y   |          |
| If logged in:          |                                                         |                                                                                                                  |     |          |
| 4                      | Click “Proceed to Checkout”                             | Redirects to Checkout page                                                                                       | Y   |          |
| If logged out:         |                                                         |                                                                                                                  |     |          |
| 5                      | Click “Proceed to Checkout”                             | Button disabled and prompt instructs user to log in or sign up                                                   | Y   |          |
| If No Items in Bag:    |                                                         |                                                                                                                  |     |          |
| 6                      | View Shopping Bag                                       | Displays messaging informing user of no items in the bag and "Keep Shopping" button                              | Y   |          |
| 7                      | Click "Keep Shopping"                                   | Redirects to All Products page                                                                                   | Y   |          |
| Checkout               |                                                         |                                                                                                                  |     |          |
| 1                      | Fill out delivery form with valid details               | Form accepts data                                                                                                | Y   |          |
| 2                      | Fill out delivery form with invalid details             | Form doesn't successfully submit and relevent field error messages shown                                         | Y   |          |
| 2                      | Check “Update profile with delivery information”        | Profile information is updated                                                                                   | Y   |          |
| 3                      | Enter payment details and click “Pay Now”               | Payment processes and redirects to Checkout Success                                                              | Y   |          |
| Checkout Success       |                                                         |                                                                                                                  |     |          |
| 1                      | View order confirmation page                            | Displays order number, email confirmation notice, and order summary                                              | Y   |          |
| 2                      | Click “Back to Home”                                    | Redirects to Home page                                                                                           | Y   |          |
| Profile                |                                                         |                                                                                                                  |     |          |
| 1                      | Update delivery information and submit                  | Success message confirms profile updated                                                                         | Y   |          |
| If user has orders:    |                                                         |                                                                                                                  |     |          |
| 2                      | View order history                                      | Displays table of all users previous orders                                                                      | Y   |          |
| 3                      | Click an order number in order history                  | Redirects to details for that order (Order History page)                                                         | Y   |          |
| If user has no orders: |                                                         |                                                                                                                  |     |          |
| 4                      | View order history                                      | Displays message informing user of no orders and "Shop Now" button                                               | Y   |          |
| 5                      | Click "Shop Now" button                                 | Redirected to products page.                                                                                     | Y   |          |
| Order History          |                                                         |                                                                                                                  |     |          |
| 1                      | Review past order details                               | Information for selected past order is displayed with message reminding the user that this is from a past order. | Y   |          |
| 2                      | Click “Back to Profile”                                 | Redirects to Profile page                                                                                        | Y   |          |
| Garden                 |                                                         |                                                                                                                  |     |          |
| 1                      | Click “Add Plant”                                       | Opens Add Garden Plant page                                                                                      | Y   |          |
| 2                      | Click a plant in the list                               | Opens Garden Plant Detail page                                                                                   | Y   |          |
| Garden Plant Detail    |                                                         |                                                                                                                  |     |          |
| 1                      | Click “Back to Garden”                                  | Redirects to My Garden page                                                                                      | Y   |          |
| 2                      | Click “Edit”                                            | Opens Edit Garden Plant page                                                                                     | Y   |          |
| 3                      | Click “Delete”                                          | Opens delete confirmation modal                                                                                  | Y   |          |
| Delete Modal           | Click "Delete" button                                   | Opens delete confirmation modal                                                                                  | Y   |          |
|                        | Click "Cancel"                                          | Modal closes without deletion                                                                                    | Y   |          |
|                        | Click "Delete"                                          | Plant is deleted, modal closes, success message dispalyed                                                        | Y   |          |
|                        | Click outside modal                                     | Modal closes                                                                                                     | Y   |          |
| Add Garden Plant       |                                                         |                                                                                                                  |     |          |
| 1                      | Submit valid form details                               | New plant is added to garden and success message shown                                                           | Y   |          |
| 2                      | Submit invalid form details                             | Form doesn't submit and relevent error messages shown.                                                           | Y   |          |
| 3                      | Click “Cancel”                                          | Returns to Garden page without saving                                                                            | Y   |          |
| Edit Garden Plant      |                                                         |                                                                                                                  |     |          |
| 1                      | Update plant details and submit                         | Changes saved and success message shown                                                                          | Y   |          |
| 2                      | Add another photo                                       | Additional photo appears in plant detail                                                                         | Y   |          |
| 3                      | Delete a photo                                          | Selected photo removed from plant                                                                                | Y   |          |

## Bugs

**Solved bugs:**

1. When submitting the checkout form when invalid post code entered, error 500 was recieved on form submission.

_Solution:_ addition of front end post code regex validation for the checkout form.

2. When adding a photo for the add/edit user garden plant form, caption and description (image_alt) were required even if no image had been uploaded.

_Solution:_ within the form set required to false for caption and description (image_alt), and within a clean function use an if statment to check for an image and if either caption or description (image_alt) aren't present to throw and error.

3. When adding or editing a plant in the users garden, if the plant details form was valid but not the plant photo form, the details form was still submitting and the page redirecting but the photo wasn't uploading

_Solution:_ check both forms are valid in the view before submitting either form.

4. If only one photo was uploaded for a user's garden plant, the carousel arrow buttons were still visible.

_Solution:_ In the plant_detail template within the "if photos" logic, use another if statement to check number of images uploaded is greater than 1 and only dislay the arrows within that statement.

**Unsolved bugs:**

1. Although invalid post codes aren't allowed in the checkout delivery form, they can be added to the profile delivery information, and therefore added by default to the checkout page when the user next goes to checkout, causing the form to be invalid.

_Future_Solution:_ Add regex validation to the profile form as well as the checkout form.

2. For the checkout and profile form, non-numerical characters can be added to the phone number field and successfully submitted in the form.

_Future_Solution:_ Add regex validation to the phone number in both the back and front-end.

## Validation

### HTML Validation:

-   There were no errors or warnings found when passing the HTML code through the [W3C](https://validator.w3.org/) validator, except for in the sign-up page, which had a few erros due to an unordered list being within a span, which caused the validator to throw an error for tags beofre and after the list. This however was code from the django allauth library, so I am unable to change it.

-   This checking was done manually by copying the HTML code from the 'Page Source' and pasting it into the validator, as authentication is required via the URL.

-   [Home Page HTML validation report](documentation/validation/index_html_validation.png)
-   [Product List Page HTML validation report](documentation/validation/product_list_html_validation.png)
-   [Product Details Page HTML validation report](documentation/validation/product_details_html_validation.png)
-   [Bag Page HTML validation report](documentation/validation/bag_html_validation.png)
-   [Checkout Page HTML validation report](documentation/validation/checkout_html_validation.png)
-   [Checkout Success Page HTML validation report](documentation/validation/checkout_success_html_validation.png)
-   [Profile Page HTML validation report](documentation/validation/profile_html_validation.png)
-   [Garden List Page HTML validation report](documentation/validation/garden_list_html_validation.png)
-   [Garden Plant Details Page HTML validation report](documentation/validation/garden_plant_detail_html_validation.png)
-   [Add Garden Plant Page HTML validation report](documentation/validation/add_garden_plant_html_validation.png)
-   [Edit Garden Plant Page HTML validation report](documentation/validation/edit_garden_plant_html_validation.png)
-   [Log In Page HTML validation report](documentation/validation/log_in_html_validation.png)
-   [Log Out Page HTML validation report](documentation/validation/log_out_html_validation.png)
-   [Sign Up Page HTML validation report](documentation/validation/sign_up_html_validation.png)

### CSS Validation:

-   No errors or warnings were found when passing through the [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator

-   [CSS Validation](documentation/validation/css_validation.png)

### JS Validation:

-   [JSHint](https://jshint.com/) was run on the JavaScript code and there were no errors found.

-   [Bag JS validation](documentation/validation/bag_js_validation.png)
-   [Stripe JS validation](documentation/validation/stripe_js_validation.png)
-   [Product List JS validation](documentation/validation/product_list_js_validation.png)

### Python Validation:

-   No errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/).
-   This checking was done manually by copying python code and pasting it into the validator.

Wild Root:

-   [WildRoot URLs PEP8](documentation/validation/wildroot_urls_python_validation.png)
-   [WildRoot Settings PEP8](documentation/validation/wildroot_setting_python_validation.png)

Bag:

-   [Bag Apps PEP8](documentation/validation/bag_apps_python_validation.png)
-   [Bag Contexts PEP8](documentation/validation/bag_contexts_python_validation.png)
-   [Bag URLs PEP8](documentation/validation/bag_urls_python_validation.png)
-   [Bag Views PEP8](documentation/validation/bag_views_python_validation.png)

Checkout:

-   [Checkout Admin PEP8](documentation/validation/checkout_admin_python_validation.png)
-   [Checkout Apps PEP8](documentation/validation/checkout_apps_python_validation.png)
-   [Checkout Forms PEP8](documentation/validation/checkout_forms_python_validation.png)
-   [Checkout Models PEP8](documentation/validation/checkout_models_python_validation.png)
-   [Checkout Signals PEP8](documentation/validation/checkout_signals_python_validation.png)
-   [Checkout URLs PEP8](documentation/validation/checkout_urls_python_validation.png)
-   [Checkout Views PEP8](documentation/validation/checkout_views_python_validation.png)

Garden:

-   [Garden Apps PEP8](documentation/validation/garden_apps_python_validation.png)
-   [Garden Forms PEP8](documentation/validation/garden_forms_python_validation.png)
-   [Garden Models PEP8](documentation/validation/garden_models_python_validation.png)
-   [Garden URLs PEP8](documentation/validation/garden_urls_python_validation.png)
-   [Garden Views PEP8](documentation/validation/garden_views_python_validation.png)

Home:

-   [Home Apps PEP8](documentation/validation/home_apps_python_validation.png)
-   [Home URLs PEP8](documentation/validation/home_urls_python_validation.png)
-   [Home Views PEP8](documentation/validation/home_views_python_validation.png)

Products:

-   [Products Admin PEP8](documentation/validation/products_admin_python_validation.png)
-   [Products Apps PEP8](documentation/validation/products_apps_python_validation.png)
-   [Products Models PEP8](documentation/validation/products_models_python_validation.png)
-   [Products URLs PEP8](documentation/validation/products_urls_python_validation.png)
-   [Products Views PEP8](documentation/validation/products_views_python_validation.png)

Profiles:

-   [Profiles Apps PEP8](documentation/validation/profiles_apps_python_validation.png)
-   [Profiles Forms PEP8](documentation/validation/profiles_forms_python_validation.png)
-   [Profiles Models PEP8](documentation/validation/profiles_models_python_validation.png)
-   [Profiles URLs PEP8](documentation/validation/profiles_urls_python_validation.png)
-   [Profiles Views PEP8](documentation/validation/profiles_views_python_validation.png)

---

## Lighthouse Report

LightHouse is a web performance testing tool that can be used to evaluate the performance of a website. The report is generated by Google Chrome.
There were some warnings about image loading which could be addressed in the future.

[Lighthouse Report](documentation/lighthouse_report.png)

---

## Compatibility

Testing was conducted on the following browsers;

-   Chrome;
-   Firefox;
-   Safari;

---

## Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/) Chrome extension.

[Home](documentation/home_responsive.png)
[Product List](documentation/product_list_responsive.png)
[Product Detail](documentation/product_detail_responsive.png)
[Shopping Bag](documentation/bag_responsive.png)

---
