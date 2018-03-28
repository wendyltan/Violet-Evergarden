#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 13:50
# @Author  : Wendyltanpcy
# @File    : emailDlg.py
# @Software: PyCharm

from violet.util import *
class EmailDialog(simpledialog.Dialog):
    """
    Common email dialog
    """
    def body(self, master):
        Label(master, text="收信人:").grid(row=0)
        Label(master, text="主题:").grid(row=1)

        self.r = StringVar()
        self.s = StringVar()
        self.e1 = Entry(master,textvariable=self.r)
        self.e2 = Entry(master,textvariable=self.s)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1
    def ok(self, event=None):
        self.apply()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def apply(self):
        if((hp.check_email_valid(self.e1.get()) and self.e2.get()) !=None):
            self.result = [self.e1.get(),self.e2.get()]
            self.cancel()
        else:
            mb.showwarning(title='注意', message='老爷您是否还没填好正确收件人和主题呢')
            self.r.set("")
            self.s.set("")
            self.e1.focus()