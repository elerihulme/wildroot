# Testing

## Manual Testing

| Page             | User Actions                                      | Expected Results                                                                                                                    | Y/N | Comments |
| ---------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --- | -------- |
| Sign Up          |                                                   |                                                                                                                                     |     |          |
| 1                | Click on Sign Up button                           | Redirection to Sign Up page                                                                                                         | Y   |          |
| 2                | Click on the Login link in the form               | Redirection to Login page                                                                                                           | Y   |          |
| 3                | Enter valid email 2 times                         | Field will only accept email address format                                                                                         | Y   |          |
| 4                | Enter valid password 2 times                      | Field will only accept password format                                                                                              | Y   |          |
| 5                | Click on Sign Up button                           | asks user to confirm email page Sends address a confirmation request email                                                          | Y   |          |
| 6                | Confirm email                                     | Redirects user to blank Sign In page                                                                                                | Y   |          |
| 7                | Sign In                                           | Redirects user to blank In page                                                                                                     | Y   |          |
| 8                | Sign In with the same email/username and password | Takes user to schedule page with pop-up confirming successful sign in. Get started button now missing in main nav, replaced by Menu | Y   |          |
| 9                | Click "Logout" button in the center of the page   | Redirects user to home page                                                                                                         | Y   |          |
| 10               | Click browser back button                         | You are still logged out                                                                                                            | Y   |          |
| Log In           |                                                   |                                                                                                                                     |     |          |
| 1                | Click on Log In button                            | Redirection to Log In page                                                                                                          | Y   |          |
| 2                | Click on the Sign Up link in the form             | Redirection to Sign Up page                                                                                                         | Y   |          |
| 3                | Enter valid email                                 | Field will only accept email address format                                                                                         | Y   |          |
| 4                | Enter valid password                              | Field will only accept password format                                                                                              | Y   |          |
| 5                | Click on Log In button                            | Redirects user to blank In page                                                                                                     | Y   |          |
| 6                | click logout button                               | Redirects user to home page                                                                                                         | Y   |          |
| 7                | Click browser back button                         | You are still logged out                                                                                                            | Y   |          |
| 8                | Click on Log In button                            | Redirection to Log In page                                                                                                          | Y   |          |
| 9                | Enter valid email                                 | Field will only accept email address format                                                                                         | Y   |          |
| 10               | Enter valid password                              | Field will only accept password format                                                                                              | Y   |          |
| 11               | Click Remember Me checkbox                        | Remembers user                                                                                                                      | Y   |          |
| 12               | Click on Log In button                            | Redirects user to blank In page                                                                                                     | Y   |          |
| 13               | Click logout button                               | Redirects user to home page                                                                                                         | Y   |          |
| 14               | Click browser back button                         | You are still logged out                                                                                                            | Y   |          |
| 15               | Click on Log In button                            | Redirection to Log In page prefilled                                                                                                | Y   |          |
| Navigation       |                                                   |                                                                                                                                     |     |          |
| 1                | Click on the logo                                 | Redirection to home page                                                                                                            | Y   |          |
| 2                | Click Store                                       | Redirection to Store page                                                                                                           | Y   |          |
| 3                | Click wishlist button                             | Redirection to wishlist page                                                                                                        | Y   |          |
| 4                | Click bag button                                  | Redirection to bag page                                                                                                             | Y   |          |
| 5                | Click Profile button                              | Redirection to Profile page                                                                                                         | Y   |          |
| 6                | Click Logout button                               | Redirection to logout page                                                                                                          | Y   |          |
| Admin Navigation |                                                   |                                                                                                                                     |     |          |
| 1                | Click Personnel dashboard                         | Dropdown menu opens                                                                                                                 | Y   |          |
| 2                | Click on Promo                                    | Redirection to Promo page                                                                                                           | Y   |          |
| 3                | Click on Emails                                   | Redirection to create email page                                                                                                    | Y   |          |
| 4                | Click Categories                                  | Redirection to Categories page                                                                                                      | Y   |          |
| 5                | Click Brands                                      | Redirection to Brands page                                                                                                          | Y   |          |
| 6                | Click on Tags                                     | Redirection to Tags page                                                                                                            | Y   |          |
| 7                | Click on Product Types                            | Redirection to Product Types page                                                                                                   | Y   |          |
| 8                | Click on Product attributes                       | Redirection to Product attributes page                                                                                              | Y   |          |
| 9                | Click on Attributes values                        | Redirection to Attributes values page                                                                                               | Y   |          |
| 11               | Click on Products                                 | Redirection to Products page                                                                                                        | Y   |          |
| 12               | Click on Users                                    | Redirection to Users page                                                                                                           | Y   |          |
| 13               | Click on Stock                                    | Redirection to Stock page                                                                                                           | Y   |          |
| 14               | Click on Orders                                   | Redirection to Orders page                                                                                                          | Y   |          |
| 15               | Click on Stock Requests                           | Redirection to Stock Requests page                                                                                                  | Y   |          |

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

-   Brave;
-   Chrome;
-   Firefox;

[Compatibility Report](documentation/validation/compatibility.pdf)

---

## Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

[Responsiveness Report](documentation/testing/responsiveness.pdf)

---
