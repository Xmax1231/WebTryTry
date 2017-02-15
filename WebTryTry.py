#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys, os, time, httplib
import re
list_http=[]  

def open_httptxt():   
    try:
        passlist = []
        list_passlist=[]
        xxx = file('dictionary.txt', 'r')
        for xxx_line in xxx.readlines():
            passlist.append(xxx_line)
        xxx.close()

        for i in passlist:
            if i not in list_passlist:
                list_passlist.append(i)

        E = 0 

        while E < len(list_passlist):
            past.append(list_passlist[E])  
            E = E + 1
    except:
        return 0

def BruteForce(host): 
    GotResponse = [301,200,302,403] #收到哪些狀態要顯示出來
    try:
        if host[-1] == "/": #去除網址尾端的斜線  google.com.tw/ <-  因為 Dictionary.txt 已經存在斜線了 -> /admin 
           host=host[0:-1]
        print '\n' + host.replace("https://","").replace("http://","") + '\n'
        for MyDict in past:
            MyDict = MyDict.replace("\n","")
            if 'https://' in host:
                connection = httplib.HTTPSConnection(host.replace("https://",""),443,timeout=10)
            else:
                host='http://' + host.replace("http://","")
                connection = httplib.HTTPConnection(host.replace("http://",""),80,timeout=10)
            connection.request("GET",MyDict)
            response = connection.getresponse()
            if response.status in GotResponse:          
                Finaldata="%s%s ---> %s %s"%(host,MyDict,response.status, response.reason)
                print Finaldata + ' 存在 !!!!!!!!!\n'
        connection.close()
        return 1
    except:
        print "[錯誤] 已經停止，可能是人為中斷或網址無法正常到達　！\n"
        pass
        return 0

if __name__=='__main__':
    print "\n===Python 網站目錄及檔案掃描工具 By Mico==="
    global  past  
    past = []
    open_httptxt()  
    target=raw_input('輸入網址 : ')
    BruteForce(target)
