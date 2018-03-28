#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 12:17
# @Author  : Wendyltanpcy
# @File    : email.py
# @Software: PyCharm
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import os

from violet import *
from violet.util import hp
import configparser
def send_common_mail(receiver,mail_content,mail_title):
    if hp.check_email_valid(receiver):
        #using configparser to load config
        config = configparser.ConfigParser()
        config.read('config.ini')
        host_server = config['DEFAULT']['HostServer']
        sender_qq = config['DEFAULT']['SenderQQ']
        pwd = config['DEFAULT']['PWD']
        sender_qq_mail = config['DEFAULT']['SenderQQMail']
        #ssl登录
        smtp = smtplib.SMTP_SSL(host_server)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        print("Mail sent success!")
    else:
        print("Please check your email address!")



