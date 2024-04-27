# Automated Email Sender

This Python script enables the automatic sending of emails using SMTP with environment-variable-based credential management. It is designed to work with Google's SMTP services but can be adapted for other SMTP providers by adjusting the server settings.

## Features

- Send emails using a simple Python function.
- Use environment variables for secure credential storage.
- Flexible SMTP server configuration.

## Prerequisites

Before you start, ensure you have the following:
- Python 3.6 or later.
- `python-dotenv` package to manage environment variables.
- A Google account with [App Passwords](https://myaccount.google.com/u/4/apppasswords) configured (if using Gmail).

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://your-repository-url
    cd your-repository-directory
    ```

2. **Install dependencies:**

    Install the required Python packages using pip:

    ```bash
    pip install python-dotenv
    ```

3. **Environment Variables:**

    Create a `.env` file in the root directory of the project and add the following line:

    ```plaintext
    EMAIL_APP_PASSWORD=YourAppPasswordHere
    ```

    Replace `YourAppPasswordHere` with the app password you generated for your email account. Follow the steps to create an app password [here](https://myaccount.google.com/u/4/apppasswords).

## Usage

To send an email, run the script with the necessary parameters:

```python
from send_email import send_emails

# Define email parameters
receiver = "receiver@example.com"
sender = "your-email@example.com"
body = "Hello, this is a test email from my automated script."
smtp = "smtp.gmail.com"
port = 587

# Send the email
send_emails(receiver, sender, body, smtp, port)
