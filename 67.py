# -*- coding: utf-8 -*-

import smtplib

mailfrom = 'Daniel Żyła'
mailto = ['dzmsgbox@gmail.com', 'danielzyla1@gmail.com']
mailsubject = 'Sending email with Python 3#$%^&*()_+!~~:"?><'
mailbody = '''
Oto treść maila. Wysyłam w celu przetestowania modułu smtplib
oraz znaków polskich i utf, AĘćęłśźźzźŻ

regards,
D. '''

messagetext = '''From:{}
Subject:{}

{}'''.format(mailfrom, mailsubject, mailbody)


user = 'dzmsgbox@gmail.com'
password = '********'
#try:
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(user, password)
server.sendmail(user, mailto, messagetext.encode('utf-8'))
server.close()
#except:
#  print('An error appeared')
