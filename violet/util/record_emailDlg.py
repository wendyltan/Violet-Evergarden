#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 13:49
# @Author  : Wendyltanpcy
# @File    : record_emailDlg.py
# @Software: PyCharm
from violet.sound_recording import recorder
from violet import sound_recognizing as sr
from violet.util import *
from violet import *
from violet import email as e

class RecordEmailDialog(simpledialog.Dialog):
    """
    Sound-record content email dialog
    """
    def body(self, master):
        Label(master, text="保存文件名:").grid(row=0)
        self.fn = StringVar()
        self.e1 = Entry(master,textvariable=self.fn)
        self.e1.grid(row=0, column=1)

        Label(master, text="采样率").grid(row=1)
        self.np = StringVar()
        self.np.set(0)
        Label(master,textvariable=self.np).grid(row=1, column=1)

        Label(master, text="剩余时间").grid(row=2)
        self.tc = StringVar()
        self.tc.set(60)
        Label(master, textvariable=self.tc).grid(row=2, column=1)

        Label(master, text="收信人:").grid(row=3)
        self.r = StringVar()
        self.e3 = Entry(master, textvariable=self.r)
        self.e3.grid(row=3, column=1)

        Label(master, text="主题:").grid(row=4)
        self.s = StringVar()
        self.e4 = Entry(master, textvariable=self.s)
        self.e4.grid(row=4, column=1)

        return self.e1

    def ok(self, event=None):
        self.apply()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def apply(self):
        if(self.fn.get()!="" and hp.check_email_valid(self.e3.get()) and self.e4.get() != None):
            rec = recorder()
            for example,time_count in rec.record():
                #显示当前采样率
                self.np.set(example)
                self.tc.set(time_count)
                self.update_idletasks()
            filename = self.fn.get()+'.wav'
            rec.savewav("violet/wave/"+filename)
            success_or_not = sr.write_text_file(filename=filename)
            if success_or_not:
                mb.showinfo(title='恭喜', message='您的话我记下来了,会帮您传达')
                self.result = [self.e3.get(), self.e4.get()]
                # 读取文字并发送邮件
                self.content = hp.get_file_content('violet/speech/text.txt')
                e.send_common_mail(self.e3.get(), self.content, self.e4.get())
                mb.showinfo(title='恭喜', message='老爷您的信件我已经帮忙送到了')
                self.cancel()
            else:
                mb.showwarning(title='注意', message='请老爷您用中文再陈述一遍')
        elif not hp.check_email_valid(self.e3.get()):
            mb.showwarning(title='注意', message='老爷您的收件人地址看起来不是合法的呢')
            self.r.set("")
            self.e3.focus()
        else:
            mb.showwarning(title='注意', message='老爷您是否还没填好相关信息呢')
            self.e1.focus()