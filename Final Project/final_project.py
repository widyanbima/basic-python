import os
import getpass
import smtplib  
from email.mime.multipart import MIMEMultipart #https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
from email.mime.text import MIMEText 

email_pengirim = 'untukcobacoba47@gmail.com' 
daftar_penerima = 'penerima.txt'

def read_file(nama_file):
    with open(nama_file) as file: #https://www.w3schools.com/python/python_file_open.asp
        contents = file.readlines()
    return [item.strip() for item in contents]    
	
def send_email(alamat_penerima, password):
    msg = MIMEMultipart()
    msg['From'] = email_pengirim
    msg['To'] = ','.join(alamat_penerima)
    msg['Subject'] = subjek
    msg.attach(MIMEText(body_email))
	
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email_pengirim, password) 
    server.send_message(msg)
    server.quit()
	
def get_password(keterangan):
    while True:
        password = getpass.getpass('{}: '.format(keterangan))#https://docs.python.org/3/library/getpass.html
        if password != "":
            break
    return password

def get_string(keterangan):
    while True:
        string = input('{}: '.format(keterangan))#https://docs.python.org/3/library/getpass.html
        if string != "":
            break
    return string

if __name__ == '__main__':
    password = get_password("Masukkan password")
    subjek = get_string("Subjek")
    body_email = get_string("Isi pesan")
    try:
        alamat_penerima = read_file(daftar_penerima)
        print(f'Pengirim: {email_pengirim}')
        print(f'Penerima:')    
        for alamat_email in alamat_penerima:
            print(alamat_email)        
        print()
        print('\nSedang mengirim...')
        send_email(alamat_penerima, password)        
        print('Berhasil terkirim.')
    except Exception as e:
        print(f'Ada yang salah\n{e}')
    os.system('pause')
