from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

def send_mail(lst_text, subject='', lst_recipients = ['kotvickiy@inbox.ru']):  # subject это тема письма
    try:
        server = 'smtp.mail.ru'

        # user = 'mikhail.bykov86@mail.ru'
        # password = 'jkGHv96789JKGH.m'
        # sender = 'mikhail.bykov86@mail.ru'
        # recipients = ['m@wmob.eu', 'zlokovar@gmail.com', 'kotvickiy@inbox.ru']

        # user = 'kotvickiy@inbox.ru'
        # password = '4zHn2MWt8aaUDaTaTMMX'
        # sender = 'kotvickiy@inbox.ru'
        # recipients = ['kotvickiy@inbox.ru']
        
        user = 'smtplib@inbox.ru'
        password = '9p89Awum9XPNZNcg3BeH'
        sender = 'smtplib@inbox.ru'
        recipients = lst_recipients
        
        text = ''
        for i in lst_text:
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
        send_mail(lst_text, subject=subject)
    except Exception as ex:
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, send_mail: {ex}")
        send_mail(lst_text, subject=subject)
