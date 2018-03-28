#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 13:15
# @Author  : Wendyltanpcy
# @File    : helper.py
# @Software: PyCharm
import re
def check_email_valid(email):
    pattern = re.compile("([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)")
    result = re.match(pattern,email)
    if result and email!="915889513@qq.com":#can not be my email address !
        print("Email valid!")
        return result
    else:
        print("Invalid email!")
        return result
def get_audio_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def get_file_content(filePath):
    with open(filePath, 'r',encoding='utf-8') as fp:
        return fp.readline()

