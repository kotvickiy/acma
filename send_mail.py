import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(list_text, subject=''):  # subject это тема письма
    server = 'smtp.mail.ru'
    user = 'CheckAustralia@mail.ru'
    password = 'uyOWGV6btZ3RgDL3sawv'

    sender = 'CheckAustralia@mail.ru'
    recipients = ['kotvickiy@inbox.ru']  # 'm@wmob.eu', 'zlokovar@gmail.com'
    
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
