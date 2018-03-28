#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 12:18
# @Author  : Wendyltanpcy
# @File    : core.py
# @Software: PyCharm
from violet import gui
from violet.util import tk
if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('500x680')
    gui = gui(root)
    gui.master.title('Violet')
    gui.mainloop()

