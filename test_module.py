#-*- coding: UTF-8 -*-
'''
Created on 2017��2��25��

@author: new
'''
import urllib
import re
import os
import chardet
from operator import pos


def getImg_html(html):
    global num_pic_savehtml
    x=0
    reg = r'src="(.+?\.jpg)" style'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    #print imglist

    for imgurl in imglist:
        if imgurl[:7]==r'http://':
            wholeurl = imgurl
            #continue
        else:
            wholeurl = 'http://www.hdbxsy.com'+imgurl
            
        
        local = get_local_name(wholeurl, g_local_path)
        check_local_path(local)
        
        print 'whole_url_pic=%s' %(wholeurl)
        print 'local_pic=%s' %(local)

        try:
            urllib.urlretrieve(wholeurl,local)
        except:
            pass
        x+=1
        num_pic_savehtml += 1

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def check_local_path(local):
    pos = local.rfind('/')
    local_path = local[:pos]
    print local
    print pos
    print local_path
    if(not(os.path.exists(local_path) )):
        os.makedirs(local_path)

def get_local_name(url, local_root_path):
    len_host = len(r'http://www.hdbxsy.com/')
    local = local_root_path+url[len_host:]
    print 'url local'
    print url
    print local
    return local

def saveHtml_sub(html):
    global num_html_savehtml
    global g_local_path
    #<a href="/dsb/20170401/8587.html" title="鐗硅壊璇剧▼鈥斺�旈�氬悜鏁板锛堝仠杞︽柟妗�6鐨勫垎鍚堬級">
    #reg_url = r'href="(.+?\.html)" title="(.+)"(.|\n)*div class="newsdate">(201\d-\d\d-\d\d)</div>'
    reg_url = r'href="(.+?\.html)"'
    htmlre = re.compile(reg_url)
    htmllist = re.findall(htmlre,html)
    
    #htmllist=re.finditer(r'href="(.+?\.html)" title="(.+)"/[ -~]/<div class="newsdate">(201/d-/d/d-/d/d)</div>',html,re.S)
    
    
    print htmllist
    x = 0
    for htmlurl in htmllist:
        #print 'len=%d' %(len(htmlurl))
        #urllib.urlretrieve('http://www.hdbxsy.com'+imgurl,'wangch_%s.jpg' % x)
        wholeurl = 'http://www.hdbxsy.com'+htmlurl
        #print 'ddddate=%s,%s,%s,%s,%s' %(htmlurl[0], htmlurl[1], htmlurl[2], htmlurl[3], htmlurl[3])
        local = get_local_name(wholeurl, g_local_path)
        check_local_path(local)
        urllib.urlretrieve(wholeurl, local, callBack)
        
        print 'whole_url_pic=%s' %(wholeurl)
        print 'local_pic=%s' %(local)
        
        html_sub = getHtml(wholeurl)
        print wholeurl
        getImg_html(html_sub)
        

        x+=1
        num_html_savehtml+=1
        
    print 'num_html_sub=%d, total=%d' %(x, num_html_savehtml) 



def getImg_pic(html, name, mydate):
    global num_pic
    x=0
    reg = r'src="(.+?\.jpg)" style'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    #print imglist

    for imgurl in imglist:
        if imgurl[:7]==r'http://':
            wholeurl = imgurl
        else:
            wholeurl = 'http://www.hdbxsy.com'+imgurl
            
        print name
        print '%s_%s_%d.jpg, %s' %(mydate, name,x, imgurl)

        try:
            urllib.urlretrieve(wholeurl,'%s_%s_%d.jpg' %(mydate, name.decode('utf-8').encode('gbk'), x))
        except:
            pass
        x+=1
        num_pic += 1

    print '%s: totalx=%d img, total_total=%d pic' %(name,x, num_pic)
        
            
def getHtml_sub(html):
    global num_html
    #reg_url = r'href="(.+?\.html)" title="(.+)"(.|\n)*div class="newsdate">(201\d-\d\d-\d\d)</div>'
    reg_url = r'href="(.+?\.html)" title="(.+)".+\n.+(201\d-\d\d-\d\d)'
    htmlre = re.compile(reg_url)
    htmllist = re.findall(htmlre,html)
    
    #htmllist=re.finditer(r'href="(.+?\.html)" title="(.+)"/[ -~]/<div class="newsdate">(201/d-/d/d-/d/d)</div>',html,re.S)
    
    
    print htmllist
    x = 0
    for htmlurl in htmllist:
        print 'len=%d' %(len(htmlurl))
        #urllib.urlretrieve('http://www.hdbxsy.com'+imgurl,'wangch_%s.jpg' % x)
        wholeurl = 'http://www.hdbxsy.com'+htmlurl[0]
        #print 'ddddate=%s,%s,%s,%s,%s' %(htmlurl[0], htmlurl[1], htmlurl[2], htmlurl[3], htmlurl[3])
        html_sub = getHtml(wholeurl)
        getImg_pic(html_sub, htmlurl[1], htmlurl[2])
        print wholeurl
        print htmlurl[1]
        print htmlurl[2]
        x+=1
        num_html+=1
        
    print 'num_html_sub=%d, total=%d' %(x, num_html)      

def callBack(a,b,c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print '%.2f%%' % per

g_local_path = r'k:/00.tmp/'         
num_pic = 0  
num_html = 0    
num_pic_savehtml = 0  
num_html_savehtml = 0        
def test():
    global num_pic
    global num_html
    global num_pic_savehtml
    global num_html_savehtml    
    global g_local_path
    
    
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
        
        #
        local = get_local_name(url, g_local_path)
        check_local_path(local)
        urllib.urlretrieve(url, local, callBack)
        
        html = getHtml(url)
        saveHtml_sub(html)
        getHtml_sub(html)
        
    print 'total subhtml=%d, total pic=%d' %(num_html, num_pic)
    print 'total subhtml_save=%d, total pic_save=%d' %(num_pic_savehtml, num_html_savehtml)
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