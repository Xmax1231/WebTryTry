#!/usr/bin/env python
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
    GotResponse = [301,200,302,403] #What httpStatus want to print
    try:
        if host[-1] == "/": #Get rid of / , google.com.tw/ <-  Bks Dictionary.txt already exist -> /admin 
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
                print Finaldata + ' is Exists !!!!!!!!!\n'
        connection.close()
        return 1
    except:
        print "[Error] Stopped, Cause manually interrupt or URL Can't arrive !\n"
        pass
        return 0

if __name__=='__main__':
    print "\n===Python Web Directories and Files Scanner By Mico==="
    global  past  
    past = []
    open_httptxt()  
    target=raw_input('Input target URL : ')
    BruteForce(target)
