import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(list_text, subject=''):  # subject это тема письма
    server = 'smtp.mail.ru'
    user = 'mikhail.bykov86@mail.ru'
    password = 'jkGHv96789JKGH.m'

    sender = 'mikhail.bykov86@mail.ru'
    recipients = ['m@wmob.eu', 'zlokovar@gmail.com', 'kotvickiy@inbox.ru']
    # recipients = ['kotvickiy@inbox.ru']
    
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
