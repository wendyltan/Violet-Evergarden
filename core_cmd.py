#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:40
# @Author  : Wendyltanpcy
# @File    : core_cmd.py
# @Software: PyCharm

import click
from violet import *

@click.group()
def violet():
    pass

@violet.command()
@click.option('--name',prompt='Enter your name here',
              help='Greet to given name')
def greet(name):
    click.echo('Hello %s' % name)

@violet.command()
@click.option('--receiver',prompt='enter the receiver here',help='add your receiver')
@click.option('--subject',prompt='enter the subject here',help='add your subject')
@click.option('--mailbody',prompt='enter the body here',help='add your mail body')
def email(receiver,mailbody,subject):
    if hp.check_email_valid(receiver):
        # email is valid
        e.send_common_mail(receiver,mailbody,subject)
    else:
        click.echo('Invalid email format!try again...')


@violet.command()
@click.option('--filename',prompt='enter the audio filename',help='audio file name')
def record(filename):
    rec = rc()
    for example, time_count in rec.record():
        # 显示当前采样率
        click.echo(example)
        click.echo(time_count)
    filename = filename + '.wav'
    rec.savewav('violet/wave/'+filename)
    click.echo('audio file save success!')

@violet.command()
@click.option('--audiopath',prompt='enter audio filename ,make sure you have put in under wave dir',help='tranform audio to textfile')
def audio2text(audiopath):
    if not audiopath.endswith('.wav'):
        click.echo('you offered invalid audio filename!')
    else:
        if sr.write_text_file(audiopath):
            click.echo('text file generate success!check your file under speech/')
        else:
            click.echo('something wrong happened,please try again')

if __name__ == '__main__':
    violet()
