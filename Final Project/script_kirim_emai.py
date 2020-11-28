import smtplib
from getpass import getpass


sender = 'widyanbima@gmail.com'
recipient = 'adi.python.test.2020@gmail.com'
password = ''
subject = 'basic-python class'
pesan = 'Hi from python programming language'
message = f'Subject: {subject}\n\n{pesan}'

password = getpass(f'password email {sender} ? ')

try:
    print('sending email ...')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.close()
except Exception as ex:
    print(ex)
else:
    print('email sudah dikirim.')