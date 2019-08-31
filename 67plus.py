import smtplib
import functools

mailfrom = 'Daniel Żyła'
mailto = 'danielzyla1@gmail.com'
mailsubject = 'Sending email with Python 3#$%^&*()_+!~~:"?><'
mailbody = '''
Oto treść maila. Wysyłam z Python'a w celu przetestowania modułu smtplib
oraz znaków polskich i utf, AĘćęłśźźzźŻ

regards,
D. '''

user = 'dzmsgbox@gmail.com'
password = '********'

def send_mail_func(adFrom, subj, body, usr, passw, adTo):

    msg = '''From:{}
Subject:{}

{}'''.format(adFrom, subj, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(usr, passw)
        server.sendmail(usr, adTo, msg.encode('utf-8'))
        server.close()
        print('mail sent')
    except:
        print('An error appeared')

send_mail_func_part=functools.partial(send_mail_func, adFrom=mailfrom, usr=user, passw=password)
send_mail_func_part(subj=mailsubject, body=mailbody, adTo=mailto)