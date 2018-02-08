# authenticate and send emails from Gmail

import smtplib
import credentials

recipient = credentials.get_recipient_email()
subject = 'Test Email'
body = 'This is a test!'

# Gmail Sign In
gmail_sender = credentials.get_sender_email()
gmail_passwd = credentials.get_password()
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
except smtplib.SMTPAuthenticationError:
    print('Bad credentials.  Exiting...')
    exit(1)
except:
    print('Unknown error. Exiting...')
    exit(1)

BODY = '\r\n'.join(['To: %s' % recipient,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % subject,
                    '', body])

try:
    server.sendmail(gmail_sender, [recipient], BODY)
    print('Email sent!')
except:
    print('Error sending mail!')

erver.quit()
