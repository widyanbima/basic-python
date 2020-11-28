import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

sender = "untukcobacoba47@gmail.com"
recipient='penerima.txt'
def read_list_email(nama_file):
    with open(nama_file, 'r') as file:
        contents = file.readlines()
    return [item.strip() for item in contents] 
password = "hai,143:)"
subject = "Test email from Python"
text = "Hello from Python"

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
server.sendmail(sender, recipient, message)
server.close()
if __name__ == '__main__':
    try:
        list_data_penerima = read_list_email(recipient)
        print(f'Alamat Email Pengirim: {email_pengirim}')
        print(f'Daftar Alamat Email Penerima:')    
        for no, email_addr in enumerate(list_data_penerima):
            print(f'{no+1:2}. {email_addr}')        
        print()
        print('\nEmail Sedang Dikirim ...')
        print('Proses Pengiriman Email Selesai.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
print("Email terkirim")
