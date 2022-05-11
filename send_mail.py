from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

def send_mail(list_text, subject=''):  # subject это тема письма
    try:
        # server = 'smtp.mail.ru'
        server = 'smtp.rambler.ru'

        # user = 'mikhail.bykov86@mail.ru'
        # password = 'jkGHv96789JKGH.m'
        # sender = 'mikhail.bykov86@mail.ru'
        # recipients = ['m@wmob.eu', 'zlokovar@gmail.com', 'kotvickiy@inbox.ru']

        # user = 'kotvickiy@inbox.ru'
        # password = '4zHn2MWt8aaUDaTaTMMX'
        # sender = 'kotvickiy@inbox.ru'
        # recipients = ['kotvickiy@inbox.ru']
        
        user = 'test_acma@rambler.ru'
        password = 'ZX-spectrum1982'
        sender = 'test_acma@rambler.ru'
        recipients = ['kotvickiy@inbox.ru']
        
        text = ''
        for i in list_text:
            text += str(i).replace('.', ',').strip() + "\n"


        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender

        part_text = MIMEText(text, 'plain')

        msg.attach(part_text)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        
    except socket.gaierror:
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, send_mail: socket.gaierror")
        send_mail(list_text, subject=subject)
    except Exception as ex:
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, send_mail: {ex}")
        send_mail(list_text, subject=subject)
