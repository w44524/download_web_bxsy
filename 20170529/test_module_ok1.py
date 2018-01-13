#-*- coding: UTF-8 -*-
'''
Created on 2017��2��25��

@author: new
'''
import urllib
import re
import os
import chardet


    

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#x=98

def getImg(html, name):
    global num_pic
    x=0
    reg = r'src="(.+?\.jpg)" style'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist

    for imgurl in imglist:
        print name
        print '%s_%d.jpg, %s' %(name,x, imgurl)
        name2 = name.decode('utf-8')
        mcmd = 'copy wangch_%d.jpg %s_%d.jpg' %(x, name, x)
        #print mcmd
        mcmd2 = 'copy wangch_%d.jpg %s_-%d.jpg' %(x, name2, x)
        #print mcmd2 
        name3 = name.decode('utf-8').encode('gbk')
        mcmd3 = 'copy wangch_%d.jpg %s_--%d.jpg' %(x, name3, x)
        #print mcmd3
        name4 = name.decode('utf-8').encode('utf-8')
        mcmd4 = 'copy wangch_%d.jpg %s_---%d.jpg' %(x, name4, x)
        #print mcmd4
        
        #print chardet.detect(name)["encoding"]
        #name2=name.encode("utf-8","ignore")

        #urllib.urlretrieve('http://www.hdbxsy.com'+imgurl,'%s_%d.jpg' %(name.encode("utf-8","ignore"),x))
        try:
            urllib.urlretrieve('http://www.hdbxsy.com'+imgurl,'%s_%d.jpg' %(name.decode('utf-8').encode('gbk'), x))
        except:
            pass
        x+=1
        num_pic += 1
        #os.popen(mcmd)
        #os.popen(mcmd2)
        #os.popen(mcmd3)
        #os.popen(mcmd4)
    print '%s: totalx=%d img, total_total=%d pic' %(name,x, num_pic)
            
def getHtml_sub(html):
    global num_html
    #<a href="/dsb/20170401/8587.html" title="特色课程——通向数学（停车方案6的分合）">
    reg_url = r'href="(.+?\.html)" title="(.+)"'
    htmlre = re.compile(reg_url)
    htmllist = re.findall(htmlre,html)
    
    print htmllist
    x = 0
    for htmlurl in htmllist:
        #urllib.urlretrieve('http://www.hdbxsy.com'+imgurl,'wangch_%s.jpg' % x)
        wholeurl = 'http://www.hdbxsy.com'+htmlurl[0]
        html_sub = getHtml(wholeurl)
        getImg(html_sub, htmlurl[1])
        print wholeurl
        print htmlurl[1]
        x+=1
        num_html+=1
    print 'num_html_sub=%d, total=%d' %(x, num_html)  
    
              
num_pic = 0  
num_html = 0          
def test():
    global num_pic
    global num_html
    #html = getHtml("http://www.hdbxsy.com/dsb/20170303/7694.html")
    #print getImg(html)
    url_list = []
    url_list.append("http://www.hdbxsy.com/dsb/index.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_2.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_3.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_4.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_5.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_6.jhtml")
    url_list.append("http://www.hdbxsy.com/dsb/index_7.jhtml")
    
    for url in url_list:
        print 'URL1=%s' %(url)
        html = getHtml(url)
    
        getHtml_sub(html)
        
    print 'total subhtml=%d, total pic=%d' %(num_html, num_pic)
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