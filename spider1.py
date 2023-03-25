import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


#请求
url="http://www.glidedsky.com/level/web/crawler-basic-1"
header={
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
    "cookie":"glidedsky_session="
}
my_request=urllib.request.Request(url=url,headers=header)

#响应网页
response=urllib.request.urlopen(my_request)

#读取网页内容
html=response.read().decode("utf-8")
#print(html)
#保存文件

findnum=re.compile(r'<div class="col-md-1">(.*?)</div>',re.S)
d=[]
#分析网页
soup=BeautifulSoup(html,"html.parser")
for i in soup.find_all('div',class_="col-md-1"):
    i=str(i)
    s=re.findall(findnum,i)[0].strip()    #此处re.findall返回一个列表，需要用[]取出第一个字符  #用strip()方法去除字符串首尾的空格或换行
    d.append(int(s))
print(sum(d))
#结果291130