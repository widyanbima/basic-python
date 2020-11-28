import os
import getpass
import smtplib  
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 
from email.mime.image import MIMEImage 


nama_file_daftar_email_address_target = 'penerima.txt' 
	

email_pengirim = 'untukcobacoba47@gmail.com' 
	

sample_nama_file_pdf = 'Financial Performance Analysis.pdf'
sample_nama_file_image = 'stevedoring.png'
sample_nama_file_text = 'penerima.txt'
	

	

attach_file_pdf = False
attach_file_image = False
attach_file_text = False
	

	

isi_pesan_email = \
   'Ini adalah sample body message.\nAnda Bisa Ubah Isi Pesan Email Sesuai dengan yang anda inginkan\n\nthanks.\n\nRgds\nAdi'
	

def read_file_target_email_address(nama_file):
    with open(nama_file, 'r') as file:
        contents = file.readlines()
    return [item.strip() for item in contents]    
	

def send_email_with_attachment(list_data_penerima:list, your_email_password:str):
    msg = MIMEMultipart()
    msg['From'] = email_pengirim
    msg['To'] = ','.join(list_data_penerima)
    msg['Subject'] = 'Hahahahahaha'
    body = isi_pesan_email
    msg.attach(MIMEText(body, 'plain'))
	

    if attach_file_pdf:
        lampiran1 = MIMEApplication(open(sample_nama_file_pdf, 'rb').read())
        lampiran1.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_pdf)
        msg.attach(lampiran1)
    
    if attach_file_image:
        fp = open(sample_nama_file_image, 'rb')
        lampiran2 = MIMEImage(fp.read())
        lampiran2.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_image)
        fp.close()
        msg.attach(lampiran2)
	

    if attach_file_text:
        lampiran3 = MIMEText(open(sample_nama_file_text, 'r').read())
        lampiran3.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_text)
        msg.attach(lampiran3)
	    
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email_pengirim, your_email_password) 
    server.send_message(msg)
    server.quit()
	

	

if __name__ == '__main__':
    try:
        list_data_penerima = read_file_target_email_address(nama_file_daftar_email_address_target)
        os.system('cls')
        print('Script Python Kirim Email.')
        print('--------------------------')
        print(f'Alamat Email Pengirim: {email_pengirim}')
        print(f'Daftar Alamat Email Penerima:')    
        for no, email_addr in enumerate(list_data_penerima):
            print(f'{no+1:2}. {email_addr}')        
        print()
        while True:
            ans = input('Kirim Sample Attachment File PDF [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_pdf = True if ans == 'y' else False
        print()
        while True:
            ans = input('Kirim Sample Attachment File Image [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_image = True if ans == 'y' else False
        print()
        while True:
            ans = input('Kirim Sample Attachment File Text [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_text = True if ans == 'y' else False
        print()
        while True:
            your_email_password = getpass.getpass('Masukkan Password Alamat Email Pengirim ? ')
            if your_email_password != "":
                break
        print('\nEmail Sedang Dikirim ...')
        send_email_with_attachment(list_data_penerima, your_email_password)        
        print('Proses Pengiriman Email Selesai.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
