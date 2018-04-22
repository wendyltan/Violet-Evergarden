#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 22:47
# @Author  : Wendyltanpcy
# @File    : loveDlg.py
# @Software: PyCharm
from tkinter import Button

from violet.util import *
from violet.wilove import readQuote, getRanQuote

class LoveDialog(simpledialog.Dialog):
    """
    Common love dialog
    """
    def body(self, master):
        self.v = StringVar()
        self.love_sentence = Label(master, textvariable=self.v).grid(row=0)
        self.ran_sentences = Button(master,text="What is love",command=self.apply).grid(row=1)
        return self.love_sentence

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def apply(self):
        #change label here:
        quotes = readQuote()
        if quotes != None:
            self.v.set(getRanQuote(quotes))


