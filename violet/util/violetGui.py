#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 7:57
# @Author  : Wendyltanpcy
# @File    : violetGui.py
# @Software: PyCharm


from violet.util import *


class violetGui(tk.Frame):
    """
    Main gui for violet
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        canvas = tk.Canvas(self.master,
                        width=500,
                        height=605,
                        bg='white')
        # save the photo as a value or we can't see the photo!
        self.im = ImageTk.PhotoImage(file="img/violet.jpg")
        canvas.create_image(250, 300,image=self.im)
        canvas.pack()

        self.button = tk.Button(self.master,text="确认邮件信息",command=self.confirm_enter_text,state='disabled')
        self.button.pack(fill='x')

        self.e_text = StringVar()
        self.entry = tk.Entry(self.master,textvariable=self.e_text,state='disabled')
        self.entry.pack(fill='both',expand=1)

        # add menu
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        #菜单设置
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='菜单', menu=filemenu)
        filemenu.add_command(label='语音文字', command=self.record_sound)
        filemenu.add_command(label='文字邮件', command=self.send_email)
        filemenu.add_separator()
        filemenu.add_command(label='关于', command=self.about)
        filemenu.add_command(label='退出', command=self.master.quit)

        filemenu2 = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='设置',menu = filemenu2)
        filemenu2.add_command(label='全局设置', command=self.config_all)

    def confirm_enter_text(self):
        if self.e_text.get() !="":
            e.send_common_mail(self.temp[0],self.e_text.get(),self.temp[1])
            self.button['state'] = 'disabled'
            self.e_text.set("")
            self.entry['state'] = 'disabled'
            mb.showinfo(title='恭喜',message='老爷的信息我收到了，会替您传达')
        else:
            mb.showwarning(title='注意', message='老爷是不是还没填好信息啊')
            self.e_text.set("")

    def record_sound(self):
        r = RecordEmailDialog(self.master)

    def send_email(self):
        d = EmailDialog(self.master)
        if d.result!=None:
            #启用按钮
            if self.button['state'] == 'disabled' and self.entry['state'] == 'disabled':
                self.button['state'] = 'normal'
                self.entry['state'] = 'normal'
            self.temp = d.result

    def config_all(self):
        print("doing basic config here!")


    def about(self):
        mb.showinfo(title='关于', message='您好，无论客人在何方，\n只要有需要，我就替您传达信息')  # 提示信息对话窗

