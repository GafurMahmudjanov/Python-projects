import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Mahmudjanov Gafur'
who = email['to'] = 'who_do_you_want_to_send_to@gmail.com'
email['subject'] = 'You won 1.000.000 dollors!'

email.set_content('Here you can write the content of your email')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Your_email_address','Your_password')
    smtp.send_message(email)
    print('all good Boss!')