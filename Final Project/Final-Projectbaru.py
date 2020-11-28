import smtplib

sender = "aaaa@gmail.com"
recipient = "bbbb@gmail.com"
password = "cccc"
subject = "Test email from Python"
text = "Hello from Python"

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
server.sendmail(sender, recipient, message)
server.close()
print("Pesan terkirim")
