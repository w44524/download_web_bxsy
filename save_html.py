#-*- coding: UTF-8 -*-
'''
Created on 2017��2��25��

@author: new
'''
import urllib
import re
import os
import chardet



def get_local_name(url, local_root_path):
    local = url
    local[:25]=local_root_path
    print url
    print local
    
    

def callBack(a,b,c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print '%.2f%%' % per

         
def test():
    url = 'http://www.hdbxsy.com/dsb/20170401/8587.html'
    local = 'k://00.tmp//8587.html'
    print 'start'
    get_local_name(url, 'k://00.tmp//dsb//')
    urllib.urlretrieve(url, local, callBack)
    #http://www.hdbxsy.com/u/cms/www/201703/03124531f1op.jpg
    

    #print html
    
    
'''
#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)
'''    

if __name__ == '__main__':
    test()