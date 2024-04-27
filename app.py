import send_email



sender = 'sender'
receiver = 'receiver'
smtp = 'smtp.gmail.com'
port = 587
body = 'Hello'


if __name__ == '__main__':
    send_email.send_emails(sender, receiver,body, smtp, port)