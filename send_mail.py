import smtplib
from email.mime.text import MIMEText


def send_email(lst):
    msg = ''
    for i in lst:
        msg += str(i).replace('.', ',').strip() + "\n"
    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = 465
    MAIL_USERNAME = 'test-70@internet.ru'
    MAIL_PASSWORD = '6sBPYzGrhLRZmVy1xnJi'
    FROM = MAIL_USERNAME
    # TO = 'm@wmob.eu', 'zlokovar@gmail.com', 'vladkotvickiy@gmail.com'
    TO = ['kotvickiy@inbox.ru', 'vladkotvickiy@gmail.com']
    msg = MIMEText('\n {}'.format(msg).encode('utf-8'), _charset='utf-8')
    smtpObj = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
    smtpObj.ehlo()
    smtpObj.login(MAIL_USERNAME, MAIL_PASSWORD)
    smtpObj.sendmail(FROM, TO, 'Subject: _site_ \n{}'.format(msg))
    smtpObj.quit()

