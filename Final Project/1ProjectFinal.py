import getpass
import smtplib  
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

email_pengirim = 'untukcobacoba47@gmail.com' 
daftar_penerima = 'penerima.txt'

def read_file(nama_file):
    with open(nama_file, 'r') as file:
        contents = file.readlines()
    return [item.strip() for item in contents]    
	
def send_email(alamat_penerima:list, password:str):
    msg = MIMEMultipart()
    msg['From'] = email_pengirim
    msg['To'] = ','.join(alamat_penerima)
    msg['Subject'] = 'Hahahahahaha'
    msg.attach(MIMEText(body_email, 'plain'))
	
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email_pengirim, password) 
    server.send_message(msg)
    server.quit()
	
if __name__ == '__main__':
    while True:
        password = getpass.getpass('Password email: ')
        if password != "":
            break
    body_email = input("Isi pesan: ")
    try:
        alamat_penerima = read_file(daftar_penerima)
        print(f'Pengirim: {email_pengirim}')
        print(f'Penerima:')    
        for nomor, alamat_email in enumerate(alamat_penerima):
            print(f'{nomor+1:2}. {alamat_email}')        
        print()
        print('\nSedang mengirim...')
        send_email(alamat_penerima, password)        
        print('Berhasil terkirim.')
    except Exception as e:
        print(f'Ada yang salah:\n{e}')
