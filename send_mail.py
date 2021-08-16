import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(list_text):
    server = 'smtp.mail.ru'
    user = 'test-70@internet.ru'
    password = '6sBPYzGrhLRZmVy1xnJi'

    sender = 'test-70@internet.ru'
    recipients = ['kotvickiy@inbox.ru']
    subject = 'Австралия заблокировала ещё одно казино'
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
