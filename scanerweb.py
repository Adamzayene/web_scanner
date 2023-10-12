import webbrowser
import whois
import socket
from bs4 import BeautifulSoup
import requests
from requests import get
import re
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
fh='''

                                                       ___.    
  ______ ____ _____    ____   _____________  _  __ ____\_ |__  
 /  ___// ___\\__  \  /    \_/ __ \_  __ \ \/ \/ // __ \| __ \ 
 \___ \\  \___ / __ \|   |  \  ___/|  | \/\     /\  ___/| \_\ \
/____  >\___  >____  /___|  /\___  >__|    \/\_/  \___  >___  /
     \/     \/     \/     \/     \/                   \/    \/ 

[+] Robots.txt  :::: (1)
[+] Sitemap.xml  :::: (2)
[+] Get Personal Information  :::: (3)
[+] Extract IP Site ::: (4)
[+] Extract Emails ::: (5)
[+] Extract Phone Number And Information ::: (6)
[+] scan port ::: (7)
[+] Extract lens Site ::: (8)
'''
print(fh)
while True :
    s=int(input("entre your number:     "))
    if s==1 :
        url=input("enter url web site ///exemple///(www.google.com) :   ")
        go=webbrowser.open(url+'/robots.txt')
    elif s==2:
        url=input("enter url web site ///exemple///(www.google.com) :   ")
        se=webbrowser.open(url+'/sitemap.xml')
    elif s==3:
        url=input("enter  web site name ///exemple///(google.com)  :   ")
        info=whois.whois(url)
        print(info)
    elif s==4:
        url=input("enter url site ///exemple///(www.google.com) :     ")
        ip=socket.gethostbyname(url)
        print( url,"=",ip)
    elif s==5:
        url=input("enter url site ///exemple///(https://www.google.com)  :     ")
        go=get(url).text
        email=re.findall('\S+@\S+',go)
        for i in email :
            print(i)
    elif s==6:
        url=input("enter url site ///exemple///(https://www.google.com)  :     ")
        go=get(url).text
        fi=re.findall(r'[\d]{3}[\d]{3}[\d]{5}',go)
        for i in fi:
            i="+"+i
            number=phonenumbers.parse(i)
            print(i,"=",geocoder.description_for_number(number,'en'),carrier.name_for_number(number,'en'))
    elif s==7:
        s=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        url=input("enter url site ///exemple///(https://www.google.com)  :    ")
        fin=int(input("git lim for scan:     "))
        info2='''
        ======================
        PORT\tSTATE\tSERVICES         
        ======================
        '''
        print(info2)
        def pscan(port):
            try:
                con=s.connect((target,port))
                return True
            except:
                return False
        for i in range(1,fin):
            s=""
            if pscan(i):
                print(i," \tOPEN\t")
                s=s+"  "+i
            else:
                print(i," \tCLOSE\t")
        print(s)
    elif s==8:
        url=input("enter url site ///exemple///(https://www.google.com)   :     ")
        req=requests.get(url)
        bs=BeautifulSoup(req.text,"html.parser")
        for l in bs.findAll('a'):
            print(l.get('href'))
