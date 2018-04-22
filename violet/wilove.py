#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 7:56
# @Author  : Wendyltanpcy
# @File    : wilove.py
# @Software: PyCharm
import os
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def getQuotes(url, count):
    """
    Get quotes from url
    :param url: this should be https://www.brainyquote.com/topics/love
    :param count: the times that you want to scroll to the bottom of the page to load data gen by js
    :return:
    """

    # using this three line to obtain phantomjs service
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/4.0 (compatible; MSIE 5.5; windows NT)"
    )
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # or use this
    # driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs')

    driver.get(url)
    # scroll down
    js = "var q=document.body.scrollTop=12000"
    i=0
    quotes = []
    while(i<count):
        driver.execute_script(js)
        time.sleep(3)
        i+=1
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('div', class_="qti-listm")
    counter = 0
    for row in result:
        if (row.a != None):
            counter+=1
            quotes.append(row.a.img['alt'])
    print("quotes: ",counter)
    # write quotes into file
    with open("violet/love/love.txt", "w",encoding='utf-8') as f:
        for row in result:
            if (row.a != None):
                counter += 1
                line = row.a.img['alt']
                quotes.append(line)
                f.writelines(line+'\n')
    f.close()
    driver.quit()
    return quotes

def readQuote():
    """
    read Quote from file or from url
    :return:
    """
    quotes = []
    #see if love text exist,if not ,update from website...
    if os.path.exists('violet/love/love.txt'):
        with open('violet/love/love.txt','r') as f:
            for line in f.readlines():
                line.replace('\n',"")
                quotes.append(line)
        f.close()
        randex = random.randint(1, quotes.__len__())
        return quotes
    else:
        print("No original file!Getting new file...")
        url = "https://www.brainyquote.com/topics/love"
        quotes = getQuotes(url, 2)
        return quotes

def getRanQuote(quotes):
    """
    Get random one quote
    :param quotes: a list contain quotes
    :return:
    """
    randex = random.randint(1, quotes.__len__())
    return quotes[randex-1]



