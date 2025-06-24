# Deployment

The live deployed application can be found deployed on [Heroku](https://wildroot-d2d4c0901fc0.herokuapp.com/).

## Cloudinary

The site uses [Cloudinary](https://cloudinary.com/) to host all static files due to the fact that Heroku cannot.

Follow these steps in order to use Cloudinary.

Create a Cloudinary account:

-   Go to Cloudinary and sign up for a free account.

-   After signing up, you'll be provided with a "Cloudinary URL", which you'll need to integrate Cloudinary into your Django project.

Install the Cloudinary package:

-   In your terminal, run the following command to install the Cloudinary Python package: `pip3 install cloudinary`

Update settings.py:

-   In your Django project, open settings.py and add 'cloudinary' to the INSTALLED_APPS list:
    ` INSTALLED_APPS = [
...
'cloudinary',
]`
    Add Cloudinary credentials
-   Add the following Cloudinary configuration with your Cloudinary URL from your Cloudinary account.

Update Models to Use CloudinaryField

-   Cloudinary's CloudinaryField will allow you to store images and files in Cloudinary directly from your Django models.

Migrate Changes made to any models

Configure Media Files in Production

-   Set up Heroku environment variables: Add the Cloudinary credential to your Heroku app’s config vars

## Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

-   Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the drop-down menu.
-   Your app name must be unique, and then choose a region closest to you (EU or USA) and finally, select **Create App**.
-   From the new app **Settings**, click **Reveal Config Vars** and set your environment variables.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `DATABASE_URL`          | user's own value                                                     |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | user's own value                                                     |
| `CLOUDINARY_URL`        | user's own value                                                     |
| `EMAIL_HOST_PASS`       | user's own value                                                     |
| `EMAIL_HOST_USER`       | user's own value                                                     |
| `DEFAULT_FROM_EMAIL`    | user's own value                                                     |
| `STRIPE_PUBLIC_KEY`     | user's own value                                                     |
| `STRIPE_SECRET_KEY`     | user's own value                                                     |

Heroku needs two additional files in order to deploy properly.

-   requirements.txt
-   Procfile

You can install this project's **requirements** (where applicable) using:

-   `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs to be updated using:

-   `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

-   `echo web: gunicorn app_name.wsgi > Procfile`
-   _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

-   Under the **Deploy** tab select GitHub as your deploy method and connect it to your repository.
-   Within the **Manual Deploy** section select your required branch and click deploy.

## Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

-   `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault('SECRET_KEY', "user's own value")
os.environ.setdefault('DEVELOPMENT', '1')
os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault('STRIPE_PUBLIC_KEY', "user's own value")
os.environ.setdefault('STRIPE_SECRET_KEY', "user's own value")

```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

-   Start the Django app: `python3 manage.py runserver`
-   Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
-   Make any necessary migrations: `python3 manage.py makemigrations`
-   Migrate the data to the database: `python3 manage.py migrate`
-   Create a superuser: `python3 manage.py createsuperuser`
-   Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
-   Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/elerihulme/wildroot)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/elerihulme/wildroot`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/elerihulme/wildroot)

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/elerihulme/wildroot)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Stripe

[Stripe](https://stripe.com) was used to process the payments. The functionality for this came from the Boutique Ado walkthrough and I did not vary from that walkthrough. Stripe uses a published key and a secret key in order for it to work. The secret key is not something that is only available to the creator. These keys are set in my Heroku config settings.

### Stripe deployment

This project uses [Stripe](https://stripe.com) to handle the e-commerce payments.

Create a Stripe account and login, follow these series of steps to get your project connected.

-   From your Stripe dashboard, click to expand the "Get your test API keys".
-   You'll have two keys here:
    -   `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
    -   `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

### Gmail - email confirmation

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

-   Click on **Account Settings** in the top-right corner of Gmail.
-   Click on the **Accounts and Import** tab.
-   Within the "Change account settings" section, click on the link for **Other Google Account settings**.
-   From this new page, select **Security** on the left.
-   Select **2-Step Verification** to turn it on.
-   Once verified, select **Turn On** for 2FA.
-   Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
-   This might prompt you once again to confirm your password and account.
-   Select **Mail** for the app type.
-   Select **Other (Custom name)** for the device type.
    -   Any custom name, such as "Django" or web-piano-academy
-   You'll be provided with a 16-character password (API key).
    -   Save this somewhere locally, as you cannot access this key again later!
    -   `EMAIL_HOST_PASS` = user's 16-character API key
    -   `EMAIL_HOST_USER` = user's own personal Gmail email address
