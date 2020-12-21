import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "mayanangappan@gmail.com"
password = 'ptnpdaucxkibqiwp'


def send_mail_to(receiver_email, user_id):
    subject = "CyberHack Task From EIC Hub, Algappa University"
    body = "Your User ID is " + \
        str(user_id)+",Password is your mobile number that your registed.\n\nGood Luck"
    msg = f'Subject:{subject}\n\n{body}'

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
