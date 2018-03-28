#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 21:40
# @Author  : Wendyltanpcy
# @File    : sound_recognizing.py
# @Software: PyCharm

from aip import AipSpeech
from violet import *
from violet.util import *

APP_ID = '10981060'
API_KEY = '3oZ37nGv3NG1HgXC3S2BvnhF'
SECRET_KEY = '503cf96d2e36b4f6ebf33c2e1653fd40'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def write_text_file(filename):
    result = client.asr(hp.get_audio_content('violet/wave/'+filename), 'wav', 8000, {
        'lan': 'zh',
    })
    try:
        # 有时候这句话出错
        # print(result)
        with open('violet/speech/text.txt','w',encoding='utf-8') as f:
            f.writelines(result['result'])
        return True
    except KeyError:
        print('请确保您使用中文进行语音输入并且声音适中')
        return False