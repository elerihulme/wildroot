# Testing

## Manual Testing

| Page                | User Actions                          | Expected Results                                                                    | Y/N | Comments |
| ------------------- | ------------------------------------- | ----------------------------------------------------------------------------------- | --- | -------- |
| Sign Up             |                                       |                                                                                     |     |          |
| 2                   | Click on the Login link in the form   | Redirection to Login page                                                           | Y   |          |
| 3                   | Enter valid email                     | Field will only accept valid email address format                                   | Y   |          |
| 3                   | Enter valid username                  | Field will only accept valid username format                                        | Y   |          |
| 4                   | Enter valid password twice            | Field will only accept valid password format and matching passwords                 | Y   |          |
| 5                   | Click on Sign Up button               | Redirects user to confirm email page and sends address a confirmation request email | Y   |          |
| 6                   | Confirm email                         | Redirects user to blank Sign In page                                                | Y   |          |
| Log In              |                                       |                                                                                     |     |          |
| 2                   | Click on the Sign Up link in the form | Redirection to Sign Up page                                                         | Y   |          |
| 3                   | Enter valid email                     | Field will only accept email address format                                         | Y   |          |
| 4                   | Enter valid password                  | Field will only accept password format                                              | Y   |          |
| 5                   | Click on Log In button                | Redirects user to blank In page                                                     | Y   |          |
| 6                   | click logout button                   | Redirects user to home page                                                         | Y   |          |
| 7                   | Click browser back button             | You are still logged out                                                            | Y   |          |
| 8                   | Click on Log In button                | Redirection to Log In page                                                          | Y   |          |
| 9                   | Enter valid email                     | Field will only accept email address format                                         | Y   |          |
| 10                  | Enter valid password                  | Field will only accept password format                                              | Y   |          |
| 11                  | Click Remember Me checkbox            | Remembers user                                                                      | Y   |          |
| 12                  | Click on Log In button                | Redirects user to blank In page                                                     | Y   |          |
| 13                  | Click logout button                   | Redirects user to home page                                                         | Y   |          |
| 14                  | Click browser back button             | You are still logged out                                                            | Y   |          |
| 15                  | Click on Log In button                | Redirection to Log In page prefilled                                                | Y   |          |
| Log Out             |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Navigation          |                                       |                                                                                     |     |          |
| 1                   | Click on the logo                     | Redirection to home page                                                            | Y   |          |
| Footer              |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Home                |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Products            |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Product Detail      |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Bag                 |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Checkout            |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Checkout Success    |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Profile             |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Order History       |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Garden              |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Garden Plant Detail |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Add Garden Plant    |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Edit Garden Plant   |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |
| Admin               |                                       |                                                                                     |     |          |
| 1                   |                                       |                                                                                     | Y   |          |

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
