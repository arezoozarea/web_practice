# import socket
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print (data.decode())
# mysock.close()
#----------------------------------------------
# import urllib
# fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.decode().strip()
#     for word in words:
#         counts[word] = counts.get(word,0)+1
# print words
# large_num = -1
# large_word = None
# for k,v in counts.items():
#     if large_num < v:
#         large_num = v
#         large_word = k
# print large_word,large_num
# ---------------------------
import BeautifulSoup
import requests
url = raw_input('enter your url:')
fhand = requests.get(url)
soup =BeautifulSoup.BeautifulSoup(fhand.text)
tags = soup('a')
for tag in tags:
    print tag.get('href')
# ----------------------------------
# import requests
# from bs4 import BeautifulSoup
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname= False
# ctx.verify_mode = ssl.CERT_NONE
# import urllib
# url = raw_input('enter url:')
# html = urllib.urlopen(url,context=ctx).read()
# soup = BeautifulSoup(html,'html.parser')
# tags = soup('a')
# for tag in tags:
#     print tag.get('href',None)

