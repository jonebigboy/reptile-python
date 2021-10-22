from urllib import request,parse
import urllib
import ssl #https

context = ssl._create_unverified_context()
# response=urllib.request.urlopen('http://www.baidu.com') #可以在dota中添加post请求，urllib.request.urlopen(url, data=None, [timeout, ]*)

url='https://biihu.cc//account/ajax/login_process/'
hearers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
}
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}
data = bytes(parse.urlencode(dict),'utf-8')
context = ssl._create_unverified_context()
rep= urllib.request.Request(url, data=data, headers=hearers, method='POST')
response = request.urlopen(rep,context=context)
print(response.read().decode('utf-8'))
#urllib.request.Request(url, data=None, headers={}, method=None) 可以添加header请求
